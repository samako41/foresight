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
    "name": "Price Checker | Product Price Checker | Product Checker | Product Price Checker kiosk",
    "summary": """
        This module to allows customers to check product details using barcode.
    """,
    "version": "16.0.1",
    "description": """
        This module to allows customers to check product details using barcode.
        Price Checker
        Product Price Checker
        Product Checker
        Product Price Checker kiosk
    """,    
    "author": "CFIS",
    "maintainer": "CFIS",
    "license" :  "Other proprietary",
    "website": "https://www.cfis.store",
    "images": ["images/product_price_checker.png"],
    "category": "Sales",
    "depends": [
        "product",
        "sale_management",
    ],
    "data": [
        "security/security.xml",
        "views/product_price_checker_view.xml",
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "product_price_checker/static/src/js/**/*",
            "product_price_checker/static/src/xml/**/*",
            "product_price_checker/static/src/css/**/*",
        ],
    },   
    "installable": True,
    "application": True,
    "price"                 :  19.00,
    "currency"              :  "EUR",
    "pre_init_hook"         :  "pre_init_check",
    "uninstall_hook": "uninstall_hook",
}
