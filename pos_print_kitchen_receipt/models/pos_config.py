# -*- coding: utf-8 -*-

from odoo import fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    print_kitchen_receipt = fields.Boolean(string="Print Kitchen Receipt",default=False)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    print_kitchen_receipt = fields.Boolean(related='pos_config_id.print_kitchen_receipt', readonly=False, string='Print Kitchen Receipt')