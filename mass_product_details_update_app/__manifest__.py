# -*- coding: utf-8 -*-

{
    'name' : "Mass Products Details Update in Odoo",
    "author": "Edge Technologies",
    'version': '16.0.1.0',
    'live_test_url': "https://youtu.be/f3ialA6iwrs",
    "images":['static/description/main_screenshot.png'],
    'summary': 'Mass product qty mass product qty, location, lot number update mass update products stock mass products details update products details update product info update mass product info update mass product details update bulk product update mass stock update',
    'description' : '''
            This app helps to user for update products stock, like on hand quantity by location, also create stock with lot/serial number if not available for given location.
    

Mass product qty mass product qty, location, lot number update
Mass update products stock
Mass update products stock
Mass products details update in odoo
Products details update
Update products details update
Update product details update
Update product detail update
Update product info
Product info update
Mass product info update
Mass product details update
Managing product mass group_update_stock
Item mass changes
Manage item mass changes
Update item attributes
Update product attributes
Mass product on hand quantity update
Bulk stock update
Mass stock update
Mass product variants
Product attributes update
Managing product mass updates
Product mass updates
Batch products editor
Bulk/mass editing products
Bulk/mass editing products
Bulk product update via import
Batch products editor
Mass attribute update
Mass product quantity & price update
Bulk edit products


Mass update product stock mass update stock of product mass update

Bulk update product stock bulk update stock of product bulk update

Mass update product stock balance mass update stock balance of product mass update

Bulk update product stock balance bulk update stock balance of product bulk update


Mass update product quantity mass update quantity of product mass update

Bulk update product quantity bulk update quantity of product bulk update

Mass update product stock quantity mass update stock quantity of product mass update quantity stock

Bulk update product stock quantity bulk update stock quantity of product bulk update


Mass update product on hand stock quantity mass update on hand stock quantity of product mass update quantity on hand stock

Bulk update product on hand stock quantity bulk update on hand stock quantity of product bulk update

Mass update product on hand quantity mass update on hand quantity of product mass update on hand stock quantity

Bulk update product on hand quantity bulk update on hand quantity of product bulk update

Mass update product on hand stock mass update on hand quantity of product mass update on hand stock qty

Bulk update product on hand stock bulk update on hand quantity of product bulk update product qty

Mass update product on hand stock qty mass update on hand stock qty of product mass update qty on hand stock

Bulk update product on hand stock qty bulk update on hand stock qty of product bulk update

Mass update product on hand qty mass update on hand qty of product mass update on hand stock qty

Bulk update product on hand qty bulk update on hand qty of product bulk update qty




    ''',
    "license" : "OPL-1",
    'depends' : ['base','stock'],
    'data': [
            'security/group_update_stock.xml',
            'security/ir.model.access.csv',
            'views/mass_update_product.xml',
             ],
    'installable': True,
    'auto_install': False,
    'price': 15,
    'currency': "EUR",
    'category': 'Sales',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
