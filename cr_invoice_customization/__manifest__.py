# -*- coding: utf-8 -*-
{
    'name': "CR Invoices Customization 1",
    "description": """CR Invoice Customization""",
    "summary": "CR Invoice Customization",
    "version": "16.0.1.2.0",
    'depends': ['account'],
    'data': [
        'views/account_move_views.xml',
        'views/res_partner_bank.xml',
        'views/res_user.xml',
        'report/cr_custom_invoice.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
