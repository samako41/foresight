# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from odoo.exceptions import UserError


class StockLocationQuantity(models.TransientModel):
    _name = 'stock.location.quantity.overview'
    _description = 'Stock Location Quantity Overview'


    location_id = fields.Many2one("stock.location", string="Location", required=True)
    company_id = fields.Many2one("res.company", "Company", required=True, readonly=True, default=lambda self: self.env.company)
    hierarchy = fields.Boolean('Location hierarchy')
    product_ids = fields.Many2many('product.product', string='Products')
    all_products = fields.Boolean('All Products')



    def stock_location_overview(self):
        self.ensure_one()
        location_id = self.location_id.id
        if not self.product_ids and not self.all_products:
            raise UserError(_('select a product at least or set All Products indicator either'))
        if self.product_ids and self.all_products:
            raise UserError(_('select a product at least or set All Products indicator either'))
        if self.all_products:
            product_ids = self.env['product.product'].search([('active', '=', True), ('type', '=', 'product')])
        else:
            product_ids = self.env['product.product'].search([('active', '=', True), ('id', 'in', self.product_ids.ids), ('type', '=', 'product')])
        self.env['stock.quant']._merge_quants()
        self.env['stock.quant']._unlink_zero_quants()
        domain = [('location_id', '=', location_id), ('product_id', 'in', product_ids.ids)]
        if self.hierarchy:
            domain = [('location_id', 'child_of', location_id), ('product_id', 'in', product_ids.ids)]
        return {
            'domain': domain,
            'name': _("Stock Location Quantity Overview"),
            'res_model': 'stock.quant',
            'views': [(self.env.ref('stock_location_quantity_overview.view_stock_location_quantity_overview_tree').id, "tree"),(self.env.ref('stock.view_stock_quant_pivot').id, "pivot")],
            'context' : {'search_default_productgroup': 1},
            'type': 'ir.actions.act_window',
            }
