from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools import format_amount

class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _construct_tax_string_custom(self, price):
        currency = self.currency_id
        res = self.taxes_id.compute_all(price, product=self, partner=self.env['res.partner'])
        joined = []
        included = res['total_included']
        if currency.compare_amounts(included, price):
            joined.append(_('%s Incl. Taxes', format_amount(self.env, included, currency)))
        excluded = res['total_excluded']
        if currency.compare_amounts(excluded, price):
            joined.append(_('%s Excl. Taxes', format_amount(self.env, excluded, currency)))
        if joined:
            tax_string = f"{', '.join(joined)}"
        else:
            tax_string = " "
        return tax_string

class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def get_product_details(self, barcode):
        product = self.env['product.product'].sudo().search([('barcode', '=', barcode)])
        if not product:
            return False
        
        IrDefault = self.env['ir.default'].sudo()
        checker_pricelist = IrDefault.get('res.config.settings', "checker_pricelist_id")
        vals = {
            'product_id':  product.id, 
            'product_name' : product.name,
            'product_description_sale' : product.description_sale,
            'product_barcode': product.barcode,
            'product_code': product.default_code,
            'product_currency_id': product.currency_id.symbol,
            'product_uom_id': product.uom_id.name,
        }        
        if checker_pricelist:
            price = self.env['product.pricelist'].search([('id', '=', checker_pricelist)])._get_product_price(product, 1, False)
            tax_string = product.product_tmpl_id._construct_tax_string_custom(price)
            vals['product_price'] = price
            vals['product_price_tax'] = tax_string
        else:
            vals['product_price'] = product.list_price
            vals['product_price_tax'] = product.tax_string       
        return vals