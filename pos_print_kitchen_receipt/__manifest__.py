# -*- coding: utf-8 -*-
#################################################################################
# Author      : CFIS (<https://www.cfis.store/>)
# Copyright(c): 2017-Present CFIS.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://www.cfis.store/>
#################################################################################

{
    "name": "POS Kitchen Receipt | Customised POS Kitchen Receipt | Print POS Kitchen Receipt",
    "summary": """
        This module allows odoo pos user can Print POS Kitchen Receipt.
        """,
    "version": "16.0.1",
    "description": """
        This module allows odoo pos user can Print POS Kitchen Receipt.
        """,    
    "author": "CFIS",
    "maintainer": "CFIS",
    "license" :  "Other proprietary",
    "website": "https://www.cfis.store",
    "images": ["images/pos_print_kitchen_receipt.png"],
    "category": "Point of Sale",
    "depends": [
        "base",        
        "point_of_sale",
    ],
    "data": [
        "views/view_pos_config.xml",
    ],
    "assets": {        
        "point_of_sale.assets": [
            "/pos_print_kitchen_receipt/static/src/js/*.js",
            "/pos_print_kitchen_receipt/static/src/xml/*.xml",
        ],
    },
    "installable": True,
    "application": True,
    "price"                 :  8,
    "currency"              :  "EUR",
    "pre_init_hook"         :  "pre_init_check",
}