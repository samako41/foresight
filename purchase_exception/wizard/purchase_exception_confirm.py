# Copyright 2017 Akretion (http://www.akretion.com)
# Copyright 2020 Camptocamp SA
# Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class PurchaseExceptionConfirm(models.TransientModel):
    _name = "purchase.exception.confirm"
    _description = "Purchase exception wizard"
    _inherit = ["exception.rule.confirm"]

    related_model_id = fields.Many2one("purchase.order", "Purchase")

    def action_confirm(self):
        self.ensure_one()
        exceptions_blocking = self.exception_ids.filtered("is_blocking")
        if self.ignore and not exceptions_blocking:
            self.related_model_id.button_draft()
            self.related_model_id.ignore_exception = True
            self.related_model_id.button_confirm()
        else:
            self.related_model_id.ignore_exception = False
        return super().action_confirm()
