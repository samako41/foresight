# -*- coding: utf-8 -*-
# Part of CorTex IT Solutions Ltd.. See LICENSE file for full copyright and licensing details.

from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from lxml import etree
import json
from odoo.tools.safe_eval import safe_eval

class AccountMove(models.Model):
    _inherit = 'account.move'

    asset_ids = fields.One2many('ctx.account.asset', 'invoice_id',
                                string="Assets", copy=False)

    asset_depreciation_ids = fields.One2many('ctx.account.asset.depreciation.line', 'move_id',
                                             string='Assets Depreciation Lines')
    asset_count = fields.Integer(compute="_compute_asset_count")
    deferred_expense_count = fields.Integer(compute="_compute_asset_count")
    deferred_revenue_count = fields.Integer(compute="_compute_asset_count")

    @api.depends('asset_ids')
    def _compute_asset_count(self):
        for record in self:
            record.asset_count = len(record.asset_ids.filtered(lambda x: x.category_id.type == 'purchase'))
            record.deferred_expense_count = len(record.asset_ids.filtered(lambda x: x.category_id.type == 'expense'))
            record.deferred_revenue_count = len(record.asset_ids.filtered(lambda x: x.category_id.type == 'sale'))

    def open_asset_view(self):
        """ This action will be called from code to show asset tree view linked to current invoice
        """
        # result = self.env.ref('ctx_account_deferred_revenue_expense.action_account_expense_form').read()[0]
        result = self.env.ref('ctx_account_asset_deferred_revenue.action_ctx_account_asset_form').read()[0]
        asset_domain = safe_eval(result['domain'])
        asset_domain.append(('id', 'in', self.asset_ids.ids))
        result['domain'] = asset_domain
        result['context'] = dict(self._context,
                                 type='purchase',
                                 default_type='purchase')
        return result

    def button_draft(self):
        res = super(AccountMove, self).button_draft()
        for move in self:
            if any(asset_id.state != 'draft' for asset_id in move.asset_ids):
                raise ValidationError(_(
                    'You cannot reset to draft for an entry having a posted asset'))
            if move.asset_ids:
                move.asset_ids.sudo().write({'active': False})
                for asset in move.asset_ids:
                    asset.sudo().message_post(body=_("Vendor bill cancelled."))
        return res

    @api.model
    def _refund_cleanup_lines(self, lines):
        result = super(AccountMove, self)._refund_cleanup_lines(lines)
        for i, line in enumerate(lines):
            for name, field in line._fields.items():
                if name == 'asset_category_id':
                    result[i][2][name] = False
                    break
        return result

    def button_cancel(self):
        for move in self:
            for line in move.asset_depreciation_ids:
                line.move_posted_check = False
        return super(AccountMove, self).button_cancel()

    def action_cancel(self):
        res = super(AccountMove, self).action_cancel()
        assets = self.env['ctx.account.asset'].sudo().search(
            [('invoice_id', 'in', self.ids)])
        if assets:
            assets.sudo().write({'active': False})
            for asset in assets:
                asset.sudo().message_post(body=_("Vendor bill cancelled."))
        return res

    def action_post(self):
        for move in self:
            for depreciation_line in move.asset_depreciation_ids:
                depreciation_line.post_lines_and_close_asset()
        result = super(AccountMove, self).action_post()
        for inv in self:
            context = dict(self.env.context)
            context.pop('default_type', None)
            for mv_line in inv.invoice_line_ids.filtered(lambda line: line.move_id.move_type in ('in_invoice','out_invoice')):
                mv_line.with_context(context).asset_create()
        return result

    def open_deferred_expense_view(self):
        """ This action will be called from code to show asset tree view linked to current invoice
        """
        result = self.env.ref('ctx_account_asset_deferred_revenue.action_account_expense_form').read()[0]
        expense_domain = safe_eval(result['domain'])
        expense_domain.append(('id', 'in', self.asset_ids.ids))
        result['domain'] = expense_domain
        result['context'] = dict(self._context,
                                 type='expense',
                                 default_type='expense')
        return result

    def open_deferred_revenue_view(self):
        """ This action will be called from code to show asset tree view linked to current invoice
        """
        result = self.env.ref('ctx_account_asset_deferred_revenue.action_account_asset_asset_type_sale').read()[0]
        expense_domain = safe_eval(result['domain'])
        expense_domain.append(('id', 'in', self.asset_ids.ids))
        result['domain'] = expense_domain
        result['context'] = dict(self._context,
                                 type='sale',
                                 default_type='sale')
        return result

    @api.model
    def get_view(self, view_id=None, view_type='form', **options):
        res = super(AccountMove, self).get_view(view_id, view_type, **options)
        default_type = self._context.get('default_move_type')
        if view_type == 'form':
            if default_type is not None:
                doc = etree.fromstring(res['arch'])
                # doc = etree.XML(res['fields']['invoice_line_ids']['views']['tree']['arch'])
                if default_type == 'out_invoice':
                    node = doc.xpath(
                        "//field[@name='asset_category_id']")
                    print(node)
                    if node:
                        node[0].set('domain', "[('type','=','sale')]")
                        node[0].set('context', "{'default_type':'sale'}")
                        node[0].set('string', "Revenue Type")
                        if node[0].get('modifiers'):
                            modifiers = json.loads(node[0].get('modifiers'))
                            modifiers['column_invisible'] = [
                                ('parent.move_type', 'not in', ('out_invoice', 'in_invoice'))]
                            node[0].set("modifiers", json.dumps(modifiers))

                        res['arch'] = etree.tostring(doc)
                if default_type == 'in_invoice':
                    node = doc.xpath("//field[@name='asset_category_id']")
                    if node:
                        node[0].set('domain', "[('type','in',('purchase','expense'))]")
                        node[0].set('context', "{}")
                        node[0].set('string', "Asset/Expense Type")
                        if node[0].get('modifiers'):
                            modifiers = json.loads(node[0].get('modifiers'))
                            modifiers['column_invisible'] = [
                                ('parent.move_type', 'not in', ('out_invoice', 'in_invoice'))]
                            node[0].set("modifiers", json.dumps(modifiers))

                        res['arch'] = etree.tostring(doc)

        return res

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    asset_category_id = fields.Many2one('ctx.account.asset.category', string='Asset Category')
    asset_start_date = fields.Date(string='Asset Start Date', compute='_get_asset_date', readonly=True, store=True)
    asset_end_date = fields.Date(string='Asset End Date', compute='_get_asset_date', readonly=True, store=True)
    asset_mrr = fields.Float(string='Monthly Recurring Revenue', compute='_get_asset_date', readonly=True,
                             store=True)

    @api.model
    def default_get(self, fields):
        res = super(AccountMoveLine, self).default_get(fields)
        if self.env.context.get('create_bill') and not self.asset_category_id:
            if self.product_id and self.move_id.move_type == 'out_invoice' and \
                    self.product_id.product_tmpl_id.deferred_revenue_category_id:
                self.asset_category_id = self.product_id.product_tmpl_id.deferred_revenue_category_id.id
            elif self.product_id and self.product_id.product_tmpl_id.asset_category_id and \
                    self.move_id.move_type == 'in_invoice':
                self.asset_category_id = self.product_id.product_tmpl_id.asset_category_id.id
            self.onchange_asset_category_id()
        return res

    @api.depends('asset_category_id', 'move_id.invoice_date')
    def _get_asset_date(self):
        for rec in self:
            rec.asset_mrr = 0
            rec.asset_start_date = False
            rec.asset_end_date = False
            cat = rec.asset_category_id
            if cat:
                if cat.method_number == 0 or cat.method_period == 0:
                    raise UserError(_('The number of depreciations or the period length of '
                                      'your asset category cannot be 0.'))
                months = cat.method_number * cat.method_period
                if rec.move_id.move_type in ['out_invoice', 'out_refund']:
                    price_subtotal = rec.currency_id._convert(
                        rec.price_subtotal,
                        rec.company_currency_id,
                        rec.company_id,
                        rec.move_id.invoice_date or fields.Date.context_today(rec))

                    rec.asset_mrr = price_subtotal / months
                if rec.move_id.invoice_date:
                    start_date = rec.move_id.invoice_date.replace(day=1)
                    end_date = (start_date + relativedelta(months=months, days=-1))
                    rec.asset_start_date = start_date
                    rec.asset_end_date = end_date

    def asset_create(self):
        if self.asset_category_id:
            price_subtotal = self.currency_id._convert(
                self.price_subtotal,
                self.company_currency_id,
                self.company_id,
                self.move_id.invoice_date or fields.Date.context_today(
                    self))
            vals = {
                'name': self.name,
                'code': self.name or False,
                'category_id': self.asset_category_id.id,
                'value': price_subtotal,
                'partner_id': self.move_id.partner_id.id,
                'company_id': self.move_id.company_id.id,
                'currency_id': self.move_id.company_currency_id.id,
                'date': self.move_id.invoice_date or self.move_id.date,
                'invoice_id': self.move_id.id,
            }
            changed_vals = self.env['ctx.account.asset'].onchange_category_id_values(vals['category_id'])
            vals.update(changed_vals['value'])
            vals["first_depreciation_manual_date"] = self.move_id.invoice_date or self.move_id.date
            asset = self.env['ctx.account.asset'].create(vals)
            if self.asset_category_id.open_asset:
                if asset.date_first_depreciation == 'manual':
                    asset.first_depreciation_manual_date = asset.date
                asset.validate()
        return True

    @api.onchange('asset_category_id')
    def onchange_asset_category_id(self):
        if self.move_id.move_type == 'out_invoice' and self.asset_category_id:
            self.account_id = self.asset_category_id.account_asset_id.id
        elif self.move_id.move_type == 'in_invoice' and self.asset_category_id:
            self.account_id = self.asset_category_id.account_asset_id.id

    @api.onchange('product_uom_id')
    def _onchange_uom_id(self):
        self.onchange_asset_category_id()


    @api.onchange('product_id')
    def _onchange_product_id(self):

        for rec in self:
            if rec.product_id:
                if rec.move_id.move_type == 'out_invoice':
                    rec.asset_category_id = rec.product_id.product_tmpl_id.deferred_revenue_category_id.id
                elif rec.move_id.move_type == 'in_invoice':
                    rec.asset_category_id = rec.product_id.product_tmpl_id.asset_category_id.id


    def get_invoice_line_account(self, type, product, fpos, company):
        return product.asset_category_id.account_asset_id or super(AccountMoveLine, self).get_invoice_line_account(type, product, fpos, company)
