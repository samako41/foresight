# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _

class DayEndSummaryReport(models.Model):
    _name = "day.end.summary.report.wizard"
    _description = "Day End Summary Report"

    ni_date = fields.Date(string="Date",default=fields.Date.context_today)
    ni_product_report = fields.Boolean(string="Product IN / OUT")
    ni_report_by = fields.Selection([('none','None'),('user','User'),('partner','Partner')], default='none', string="Group By")
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)

    def ni_action_send_mail(self):
        ir_cron =self.env.ref('ni_day_end_report.scedular_send_end_day_report', False)
        template = self.env.ref('ni_day_end_report.ni_email_template_day_end_report', False)
        company_ids = self.env['res.company'].search([])
        for company_id in company_ids:
            if ir_cron and company_id.ni_enable_day_end_report and template:
                day_end_wiz_id = self.env['day.end.summary.report.wizard'].create({'ni_date':ir_cron.nextcall,'ni_report_by': company_id.ni_report_by,'company_id': company_id.id,'ni_product_report': company_id.ni_product_report})
                email_to = company_id.ni_partner_ids.ids
                model = 'day.end.summary.report.wizard'
                template.send_mail(day_end_wiz_id.id, force_send=True,email_values={'recipient_ids': email_to,'model': model})

    def action_prepare_group_dict_vals(self,records,type):
        not_none_vals,none_vals= {},{}
        for record in records:
            if type in ['sale', 'out_invoice', 'purchase', 'in_invoice','out_refund','in_refund']:
                total_amount = record.amount_total
            else:
                total_amount = record.amount
            # Not none group type
            if self.ni_report_by in ('user','partner'):
                if self.ni_report_by == 'user':
                    key = (record.user_id,record.currency_id)
                else:
                    key = (record.partner_id,record.currency_id)

                if key not in not_none_vals:
                    not_none_vals.update({key: {'amount_total': total_amount,'total_count': 1}})
                else:
                    dict_amt = not_none_vals[key]['amount_total'] + total_amount
                    dict_count = not_none_vals[key]['total_count'] + 1
                    not_none_vals.update({key: {'amount_total': dict_amt,'total_count':dict_count}})
            # None group type
            key_2 =  (record.currency_id)
            if key_2 not in none_vals:
                none_vals.update({key_2: {'amount_total': total_amount,'total_count': 1}})
            else:
                dict_amt = none_vals[key_2]['amount_total'] + total_amount
                dict_count = none_vals[key_2]['total_count'] + 1
                none_vals.update({key_2: {'amount_total': dict_amt,'total_count':dict_count}})
        return none_vals,not_none_vals

    def ni_action_print_report(self):
        return self.env.ref('ni_day_end_report.ni_day_end_summary_reports').report_action(self)

    def action_get_summary_report_tr_data(self, main_dict,details_dict,type,count_inc):
        if self.ni_report_by in ('partner','user'):
            table_row = '<tr style="background: #DCDCDC">'
        else:
            table_row = '<tr>'
        if main_dict:
            if self.ni_report_by in ('partner', 'user'):
                table_row += "<td style='height:15px;padding:5px;vertical-align:middle' class='text-center' rowspan="+str(len(main_dict))+"><b>" + str('*') + "</b></td>"
                table_row += "<td style='height:15px;padding:5px;vertical-align:middle' class='text-center' rowspan=" + str(len(main_dict)) + "> <b>" + type + "</b></td>"
            else:
                table_row += "<td style='height:15px;padding:5px;vertical-align:middle' class='text-center' rowspan="+str(len(main_dict))+">" + str(count_inc) + "</td>"
                table_row += "<td style='height:15px;padding:5px;vertical-align:middle' rowspan="+str(len(main_dict))+">" + type + "</td>"
            count=0
            for data_dict in main_dict:
                if count!=0:
                    if self.ni_report_by in ('partner', 'user'):
                        table_row += "<tr style='background: #DCDCDC'><td style='height:15px;padding:5px' ></td><td style='height:15px;padding:5px' ></td>"
                    else:
                        table_row += "<tr><td style='height:15px;padding:5px' ></td><td style='height:15px;padding:5px' ></td>"

                    count+=1
                if self.ni_report_by in ('partner', 'user'):
                    table_row+="<td style='height:15px;padding:5px;background: #DCDCDC;vertical-align:middle' class='text-center'><b>"+str(main_dict.get(data_dict).get('total_count'))+"</b></td>"
                    table_row+="<td style='height:15px;padding:5px;background: #DCDCDC;vertical-align:middle' class='text-right'><b>"+str(main_dict.get(data_dict).get('amount_total'))+str(data_dict.symbol)+"</b></td>"
                    table_row += '</tr>'
                else:
                    table_row += "<td style='height:15px;padding:5px;vertical-align:middle' class='text-center'>" + str( main_dict.get(data_dict).get('total_count')) + "</td>"
                    table_row += "<td style='height:15px;padding:5px;vertical-align:middle' class='text-right'>" + str(main_dict.get(data_dict).get('amount_total')) + str(data_dict.symbol) + "</td>"
                    table_row += '</tr>'
        if details_dict:
            details_count=0
            for details_data_dict in details_dict:
                details_count += 1
                table_row += "<tr><td style='height:15px;padding:5px;vertical-align:middle' class='text-center'>"+str(details_count)+"</td>"
                table_row += "<td style='height:15px;padding:5px;vertical-align:middle' >" + str(details_data_dict[0].name) + "</td>"
                table_row+="<td style='height:15px;padding:5px;vertical-align:middle' class='text-center' >"+str(details_dict.get(details_data_dict).get('total_count'))+"</td>"
                table_row+="<td style='height:15px;padding:5px;vertical-align:middle' class='text-right'>"+str(details_dict.get(details_data_dict).get('amount_total'))+str(details_data_dict[1].symbol)+"</td>"
                table_row += '</tr>'
        return table_row


    def action_get_summary_report_data_report(self):
        table_row = ''
        sale_ids = self.env['sale.order'].search([('state','in',('sale','done')),('date_order','>=',str(self.ni_date)+ ' 00:00:00'),('date_order','<=',str(self.ni_date)+ ' 23:59:59'),('company_id','=',self.company_id.id)])
        count_inc=0
        if sale_ids:
            count_inc+=1
            main_dict,details_dict=self.action_prepare_group_dict_vals(sale_ids,'sale')
            table_row += self.action_get_summary_report_tr_data(main_dict,details_dict,'Sale Order',count_inc)

        customer_invoice_ids = self.env['account.move'].search([('state', '=', 'posted'), ('move_type', '=', 'out_invoice'),('company_id','=',self.company_id.id),('invoice_date','=',self.ni_date)])
        if customer_invoice_ids:
            count_inc += 1
            main_dict, details_dict = self.action_prepare_group_dict_vals(customer_invoice_ids,'out_invoice')
            table_row += self.action_get_summary_report_tr_data(main_dict, details_dict, 'Customer Invoice', count_inc)

        customer_payment_ids = self.env['account.payment'].search([('state', '=', 'posted'), ('partner_type', '=', 'customer'),('company_id','=',self.company_id.id),('date','=',self.ni_date)])
        if customer_payment_ids:
            count_inc += 1
            main_dict, details_dict = self.action_prepare_group_dict_vals(customer_payment_ids, 'payment')
            table_row += self.action_get_summary_report_tr_data(main_dict, details_dict, 'Customer Payment',count_inc)

        customer_credit_ids = self.env['account.move'].search([('state', '=', 'posted'), ('move_type', '=', 'out_refund'),('company_id','=',self.company_id.id),('invoice_date','=',self.ni_date)])
        if customer_credit_ids:
            count_inc += 1
            main_dict, details_dict = self.action_prepare_group_dict_vals(customer_credit_ids, 'out_refund')
            table_row += self.action_get_summary_report_tr_data(main_dict, details_dict, 'Customer Credit Note',count_inc)

        purchase_ids = self.env['purchase.order'].search([('state', 'in', ('purchase', 'done')),('date_approve','>=',str(self.ni_date)+ ' 00:00:00'),('date_approve','<=',str(self.ni_date)+ ' 23:59:59'),('company_id','=',self.company_id.id)])
        if purchase_ids:
            count_inc += 1
            main_dict, details_dict = self.action_prepare_group_dict_vals(purchase_ids, 'purchase')
            table_row += self.action_get_summary_report_tr_data(main_dict, details_dict, 'Purchase Order',count_inc)

        supplier_invoice_ids = self.env['account.move'].search([('state', '=', 'posted'), ('move_type', '=', 'in_invoice'),('company_id','=',self.company_id.id),('invoice_date','=',self.ni_date)])
        if supplier_invoice_ids:
            count_inc += 1
            main_dict, details_dict = self.action_prepare_group_dict_vals(supplier_invoice_ids, 'in_invoice')
            table_row += self.action_get_summary_report_tr_data(main_dict, details_dict, 'Vendor Bill',count_inc)

        supplier_refund_ids = self.env['account.move'].search( [('state', '=', 'posted'), ('move_type', '=', 'in_refund'),('company_id','=',self.company_id.id),('invoice_date','=',self.ni_date)])
        if supplier_refund_ids:
            count_inc += 1
            main_dict, details_dict = self.action_prepare_group_dict_vals(supplier_refund_ids, 'in_refund')
            table_row += self.action_get_summary_report_tr_data(main_dict, details_dict, 'Vendor Refund',count_inc)

        supplier_payment_ids = self.env['account.payment'].search([('state', '=', 'posted'), ('partner_type', '=', 'supplier'),('company_id','=',self.company_id.id),('date','=',self.ni_date)])
        if supplier_payment_ids:
            count_inc += 1
            main_dict, details_dict = self.action_prepare_group_dict_vals(supplier_payment_ids, 'payment')
            table_row += self.action_get_summary_report_tr_data(main_dict, details_dict, 'Vendor Payment',count_inc)

        return table_row


    def action_get_summary_report_product(self):
        table_row = ''
        product_data_dict = {}
        if self.ni_product_report == True:
            move_ids = self.env['stock.move'].search([('state', '=', 'done'),('picking_id.picking_type_id.code', 'in', ['incoming','outgoing']),('picking_id.date_done','>=',str(self.ni_date)+ ' 00:00:00'),('picking_id.date_done','<=',str(self.ni_date)+ ' 23:59:59'),('picking_id.company_id','=',self.company_id.id)])
            if move_ids:
                for move_id in move_ids:
                    key = move_id.picking_id.picking_type_id.code
                    if key not in product_data_dict:
                        product_data_dict.update({key: {move_id.product_id: move_id.quantity_done}})
                    else:
                        if move_id.product_id not in product_data_dict[key]:
                            product_data_dict[key].update({move_id.product_id: move_id.quantity_done})
                        else:
                            quantity_added=product_data_dict[key][move_id.product_id]
                            product_data_dict[key].update({move_id.product_id:quantity_added})
                if product_data_dict:
                    for product_data in product_data_dict:
                        if product_data == 'outgoing':
                            table_row+="<tr><td style='height:15px;padding:5px;vertical-align:middle;background: #DCDCDC' class='text-center' colspan='5'>"+"<b>Outgoing</b>"+"</td>"
                        else:
                            table_row+="<tr><td style='height:15px;padding:5px;vertical-align:middle;background: #DCDCDC' class='text-center' colspan='5'>"+"<b>Incoming</b>"+"</td>"
                        count = total_qty = 0
                        for product in product_data_dict.get(product_data):
                            count += 1
                            barcode = default_code = ''
                            total_qty+=product_data_dict.get(product_data).get(product)
                            if product.barcode:
                                barcode = product.barcode
                            if product.default_code:
                                default_code = product.default_code
                            table_row += "<tr>"\
                                         "<td style='height:15px;padding:5px;vertical-align:middle' class='text-center'>"+str(count)+"</td>"\
                                         "<td style='height:15px;padding:5px;vertical-align:middle'>"+str(product.name)+"</td>" \
                                         "<td style='height:15px;padding:5px;vertical-align:middle'>"+str(default_code)+"</td>" \
                                         "<td style='height:15px;padding:5px;vertical-align:middle'>"+str(barcode)+"</td>" \
                                         "<td style='height:15px;padding:5px;vertical-align:middle' class='text-right'>"+str(product_data_dict.get(product_data).get(product))+"</td>" \
                                          "</tr>"
                        table_row += "<tr><td style='height:15px;padding:5px;vertical-align:' class='text-center' colspan='4'><b>Total</b></td><td class='text-right'><b>"+str(total_qty)+"</b></td></tr>"
        return table_row
