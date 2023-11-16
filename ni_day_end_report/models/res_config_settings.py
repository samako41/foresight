# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ni_enable_day_end_report = fields.Boolean(string='Enable Day End Report Send By Mail')
    ni_partner_ids = fields.Many2many('res.partner',string='Recipients')
    ni_mail_template_id = fields.Many2one('mail.template',string='Mail Template')
    ni_product_report = fields.Boolean(string="Product IN / OUT")
    ni_report_by = fields.Selection([('none', 'None'), ('user', 'User'), ('partner', 'Partner')], default='none',
                                    string="Group By")
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        company= self.env.company
        res['ni_enable_day_end_report'] = company.ni_enable_day_end_report
        res['ni_partner_ids'] = company.ni_partner_ids
        res['ni_product_report'] = company.ni_product_report
        res['ni_report_by'] = company.ni_report_by
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        company= self.env.company
        company.write({"ni_enable_day_end_report":self.ni_enable_day_end_report,
                       "ni_partner_ids": self.ni_partner_ids,
                       "ni_report_by": self.ni_report_by,
                       "ni_product_report": self.ni_product_report
                       })

class ResCompany(models.Model):
    _inherit = 'res.company'

    ni_enable_day_end_report = fields.Boolean(string='Enable Send Mail Daily Report')
    ni_partner_ids = fields.Many2many('res.partner', string='Recipients')
    ni_product_report = fields.Boolean(string="Product IN / OUT")
    ni_report_by = fields.Selection([('none', 'None'), ('user', 'User'), ('partner', 'Partner')], default='none',string="Group By")