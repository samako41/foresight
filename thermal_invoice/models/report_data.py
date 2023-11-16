# -*- encoding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2022. All rights reserved.

from odoo import fields, models, _
import json


class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_total_tax(self):
        tax = self.tax_totals
        return tax
