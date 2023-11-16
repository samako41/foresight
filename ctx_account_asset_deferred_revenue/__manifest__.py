# -*- coding: utf-8 -*-
# Part of CorTex IT Solutions Ltd.. See LICENSE file for full copyright and licensing details.

{
    'name': "Assets and Deferred Revenue/Expense Management",
    'version': "1.0.0",
    'summary': """Manage assets and deferred revenues/expenses,
        Keeps track of depreciation's and Deferred revenues/expenses journals, and creates corresponding journal entries""",
    'category': 'Accounting/Accounting',
    'description': """This module helps you to create assets and deferred revenues/expenses and automate
            the calculation and posting to accounting on scheduled period.
Asset 
Asset Management
Odoo Asset Management
Assets
Odoo Asset
Odoo Assets
Odoo Assets Management
Assets Management
Odoo deferred revenue
Odoo deferred expanse
deferred revenue and expense
deferred expanse
deferred revenue
    """,
    'author': 'CorTex IT Solutions Ltd.',
    'website': 'https://cortexsolutions.net',
    'license': 'OPL-1',
    'currency': 'EUR',
    'price': 95,
    'support': 'support@cortexsolutions.net',
    'depends': ['account'],
    'data': [
        'data/account_asset_data.xml',
        'security/account_asset_security.xml',
        'security/ir.model.access.csv',
        'wizard/asset_depreciation_confirmation_wizard_views.xml',
        'wizard/asset_modify_views.xml',
        'wizard/asset_sell_views.xml',
        'views/account_asset_views.xml',
        'views/account_move_views.xml',
        'views/account_deferred_expense.xml',
        'views/account_deferred_revenue.xml',
        'views/product_views.xml',
        'report/account_asset_report_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ctx_account_asset_deferred_revenue/static/src/scss/account_asset.scss',
            'ctx_account_asset_deferred_revenue/static/src/js/account_asset.js',
        ],
    },
    'demo': [],
    'installable': True,
    'auto_install': False,
    'images': ['static/description/main_screenshot.png'],
}
