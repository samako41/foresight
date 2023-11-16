# -*- coding: utf-8 -*-
##########################################################################
# Author      : Nevioo Technologies (<https://nevioo.com/>)
# Copyright(c): 2020-Present Nevioo Technologies
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
##########################################################################
{
    "name":  "Day End Summary Reports",
    "summary":  "This module allows you to generate the day end summary report of transactions.",
    "category":  "Reports",
    "version":  "15.0.1.1",
    "sequence":  1,
    "license": 'OPL-1',
    "images": ['static/description/Banner.png'],
    "author":  "Nevioo Technologies",
    "website":  "www.nevioo.com",
    "depends":  ['base','account','sale','purchase','stock'],
    'data': [
                'security/ir.model.access.csv',
                'data/ir_cron_data.xml',
                'wizard/day_end_summary_report_view.xml',
                'report/extended_layout.xml',
                'report/report.xml',
                'report/report_template_view.xml',
                'views/res_config_settings_view.xml',
                'data/send_mail.xml',
            ],
    "application":  True,
    "installable":  True,
    "auto_install":  False,
}
