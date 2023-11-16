# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductDetails(models.Model):
	_name = "product.details"
	_description = "Update Products Details"

	product_id = fields.Many2one('product.product')
	lot_id = fields.Many2one('stock.lot', "Update Lot/Serial Number")
	location_id = fields.Many2one('stock.location')
	update_quantity = fields.Float()
	current_quantity = fields.Float()
	product_update_id = fields.Many2one('product.update')


class ProductUpdate(models.Model):
	_name = 'product.update'
	_description = "Update Product Stock Details Operation"

	product_ids = fields.One2many('product.details', 'product_update_id')

	@api.model
	def default_get(self,default_fields):
		res = super(ProductUpdate, self).default_get(default_fields)
		product_obj = self.env['product.product'].browse(self._context.get('active_ids'))
		product_list = []
		for product in product_obj:
			product_data = {}
			product_data.update({'product_id':product.id, 'current_quantity':product.qty_available})
			product_list.append((0, 0,product_data))
		res.update({'product_ids':product_list})
		return res

	# update product stock details
	def product_details_update(self):
		product_list = [p.product_id.id for p in self.product_ids]
		quant_obj = self.env['stock.quant'].search([('product_id','in',product_list)])
		quant_prd_list = [q.product_id.id for q in quant_obj]
		quant_loc_list = [q.location_id.id for q in quant_obj]
		for each in self.product_ids:
			if quant_obj:
				for quant in quant_obj:
					if quant.location_id.usage == "internal":
						if quant.product_id.id == each.product_id.id and each.location_id.id == quant.location_id.id:
							quant.write({'lot_id':each.lot_id.id, 'quantity':each.update_quantity})
			if each.product_id.id not in quant_prd_list:
				self.env['stock.quant'].create({'product_id':each.product_id.id, 'location_id':each.location_id.id, 'quantity':each.update_quantity,'lot_id':each.lot_id.id})
			if each.location_id.id not in quant_loc_list and each.product_id.id in quant_prd_list:
				self.env['stock.quant'].create({'product_id':each.product_id.id, 'location_id':each.location_id.id, 'quantity':each.update_quantity,'lot_id':each.lot_id.id})
