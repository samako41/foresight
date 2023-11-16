from odoo import fields, models, api, _


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    ifsc_code = fields.Char(string="IFSC Code")
    branch_name = fields.Char("Branch")
