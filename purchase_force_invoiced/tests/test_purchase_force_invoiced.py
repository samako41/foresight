# Copyright 2019 Eficent Business and IT Consulting Services S.L.
# Copyright 2019 Aleph Objects, Inc.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields
from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged("post_install", "-at_install")
class TestPurchaseForceInvoiced(TransactionCase):
    def setUp(self):
        super(TestPurchaseForceInvoiced, self).setUp()
        self.purchase_order_model = self.env["purchase.order"]
        self.purchase_order_line_model = self.env["purchase.order.line"]
        self.account_invoice_model = self.env["account.move"]
        self.account_invoice_line = self.env["account.move.line"]
        self.invoice_account = self.env["account.account"].search(
            [
                ("account_type", "=", "expense"),
                ("company_id", "=", self.env.company.id),
            ],
            limit=1,
        )

        # Data
        product_ctg = self._create_product_category()
        self.service_1 = self._create_product("test_product1", product_ctg)
        self.service_2 = self._create_product("test_product2", product_ctg)
        self.customer = self._create_supplier("Test Supplier")

    def _create_supplier(self, name):
        """Create a Partner."""
        return self.env["res.partner"].create(
            {"name": name, "email": "example@yourcompany.com", "phone": 123456}
        )

    def _create_product_category(self):
        product_ctg = self.env["product.category"].create({"name": "test_product_ctg"})
        return product_ctg

    def _create_product(self, name, product_ctg):
        product = self.env["product.product"].create(
            {
                "name": name,
                "categ_id": product_ctg.id,
                "type": "service",
                "purchase_method": "receive",
            }
        )
        return product

    def test_purchase_order(self):
        po = self.purchase_order_model.create({"partner_id": self.customer.id})
        pol1 = self.purchase_order_line_model.create(
            {
                "name": self.service_1.name,
                "product_id": self.service_1.id,
                "product_qty": 1,
                "product_uom": self.service_1.uom_po_id.id,
                "price_unit": 500.0,
                "date_planned": fields.Date.today(),
                "order_id": po.id,
            }
        )
        pol2 = self.purchase_order_line_model.create(
            {
                "name": self.service_2.name,
                "product_id": self.service_2.id,
                "product_qty": 2,
                "product_uom": self.service_2.uom_po_id.id,
                "price_unit": 500.0,
                "date_planned": fields.Date.today(),
                "order_id": po.id,
            }
        )

        # confirm quotation
        po.button_confirm()
        # update quantities delivered
        pol1.qty_received = 1
        pol2.qty_received = 2

        self.assertEqual(
            po.invoice_status, "to invoice", "The invoice status should be To Invoice"
        )

        action = po.action_create_invoice()
        invoice = self.env["account.move"].browse(action["res_id"])
        self.assertEqual(
            po.invoice_status, "invoiced", "The invoice status should be Invoiced"
        )
        # Reduce the invoiced qty
        for line in pol2.invoice_lines:
            line.with_context(check_move_validity=False).unlink()
        self.assertEqual(
            po.invoice_status, "to invoice", "The invoice status should be To Invoice"
        )
        # We set the force invoiced.
        po.button_done()
        po.force_invoiced = True
        self.assertEqual(
            po.invoice_status, "invoiced", "The invoice status should be Invoiced"
        )
        # We remove the force invoiced.
        po.force_invoiced = False
        self.assertEqual(
            po.invoice_status, "to invoice", "The invoice status should be To Invoice"
        )
        action = po.action_create_invoice()
        invoice = self.env["account.move"].browse(action["res_id"])
        invoice_qty = sum(
            invoice.invoice_line_ids.filtered(
                lambda x: x.product_id.id == self.service_2.id
            ).mapped("quantity")
        )
        self.assertEqual(invoice_qty, 2.0)
