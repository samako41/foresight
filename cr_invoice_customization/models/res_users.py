# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class UsersView(models.Model):
    _inherit = 'res.users'

    user_signature = fields.Binary(string='Signature')
