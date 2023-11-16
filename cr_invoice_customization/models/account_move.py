# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import datetime, date, timedelta


class AccountMove(models.Model):
    _inherit = 'account.move'

    tin_number = fields.Char('TIN Number')
    service_number = fields.Char('Service Entry Number')
    Service_date_from = fields.Date('From')
    Service_date_to = fields.Date('To')
    date = fields.Date('Date')
    account_id = fields.Many2one(
        'res.partner.bank', 'Account Number',
        tracking=True,
        help='bank account')
    po_order_desc = fields.Char('Purchase Order Description')
    payment_condition = fields.Char('Pay Condition')
    vat_amount = fields.Float('VAT Amount', compute='_compute_vat_totals')

    def _compute_vat_totals(self):
        for rec in self:
            rec.vat_amount = 0
            vat = 0
            for line in rec.invoice_line_ids:
                for tax_id in line.tax_ids.filtered(lambda t: t.name == 'Output VAT - 7.5%' and t.amount == 7.5000):
                    vat += line.price_subtotal * tax_id.amount / 100
            rec.vat_amount = vat

