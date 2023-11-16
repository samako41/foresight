# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    pw_not_zero_qty = fields.Boolean(string='Restrict Zero Quantity')

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pw_not_zero_qty = fields.Boolean(related='pos_config_id.pw_not_zero_qty', readonly=False)
