# -*- coding: utf-8 -*-
{
    'name': 'POS Restrict Zero Quantity',
    'version': '1.0',
    'author': 'Preway IT Solutions',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'summary': 'This module is use to restrict zero quantity on pos order | POS Not Allowed Zero Quantity',
    'description': """
- POS Restrict to validate pos order if quantity is zero
    """,
    'data': [
        'views/pos_config.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pw_pos_restrict_zero_qty/static/src/js/ProductScreen.js',
        ],
    },
    'price': 4.0,
    'currency': "EUR",
    'application': True,
    'installable': True,
    'live_test_url': '',
    "license": "LGPL-3",
    "images":["static/description/Banner.png"],
}
