
[![Runboat](https://img.shields.io/badge/runboat-Try%20me-875A7B.png)](https://runboat.odoo-community.org/builds?repo=OCA/stock-logistics-workflow&target_branch=16.0)
[![Pre-commit Status](https://github.com/OCA/stock-logistics-workflow/actions/workflows/pre-commit.yml/badge.svg?branch=16.0)](https://github.com/OCA/stock-logistics-workflow/actions/workflows/pre-commit.yml?query=branch%3A16.0)
[![Build Status](https://github.com/OCA/stock-logistics-workflow/actions/workflows/test.yml/badge.svg?branch=16.0)](https://github.com/OCA/stock-logistics-workflow/actions/workflows/test.yml?query=branch%3A16.0)
[![codecov](https://codecov.io/gh/OCA/stock-logistics-workflow/branch/16.0/graph/badge.svg)](https://codecov.io/gh/OCA/stock-logistics-workflow)
[![Translation Status](https://translation.odoo-community.org/widgets/stock-logistics-workflow-16-0/-/svg-badge.svg)](https://translation.odoo-community.org/engage/stock-logistics-workflow-16-0/?utm_source=widget)

<!-- /!\ do not modify above this line -->

# stock-logistics-workflow

TODO: add repo description.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[delivery_procurement_group_carrier](delivery_procurement_group_carrier/) | 16.0.1.0.0 |  | Delivery Procurement Group Carrier
[purchase_stock_picking_invoice_link](purchase_stock_picking_invoice_link/) | 16.0.1.0.0 |  | Adds link between purchases, pickings and invoices
[stock_delivery_note](stock_delivery_note/) | 16.0.1.0.0 |  | This module allows to fill in a delivery note that will be displayed on delivery report
[stock_grn](stock_grn/) | 16.0.1.0.1 |  | Goods Received Note
[stock_lot_production_date](stock_lot_production_date/) | 16.0.1.0.0 |  | Stock Lot Production Date
[stock_move_line_auto_fill](stock_move_line_auto_fill/) | 16.0.1.0.2 |  | Stock Move Line auto fill
[stock_move_line_reserved_quant](stock_move_line_reserved_quant/) | 16.0.1.0.0 | [![rousseldenis](https://github.com/rousseldenis.png?size=30px)](https://github.com/rousseldenis) | This module allows to get the link from a stock move line to the reserved quant
[stock_move_propagate_first_move](stock_move_propagate_first_move/) | 16.0.1.0.1 |  | This addon propagate the picking type of the original move to all next moves created from procurement
[stock_no_negative](stock_no_negative/) | 16.0.1.0.1 |  | Disallow negative stock levels by default
[stock_owner_restriction](stock_owner_restriction/) | 16.0.1.0.0 |  | Do not reserve quantity with assigned owner
[stock_picking_auto_create_lot](stock_picking_auto_create_lot/) | 16.0.1.0.0 | [![sergio-teruel](https://github.com/sergio-teruel.png?size=30px)](https://github.com/sergio-teruel) | Auto create lots for incoming pickings
[stock_picking_back2draft](stock_picking_back2draft/) | 16.0.1.0.0 |  | Reopen cancelled pickings
[stock_picking_filter_lot](stock_picking_filter_lot/) | 16.0.1.0.0 |  | In picking out lots' selection, filter lots based on their location
[stock_picking_group_by_base](stock_picking_group_by_base/) | 16.0.1.0.0 |  | Allows to define a way to create index on extensible domain
[stock_picking_group_by_max_weight](stock_picking_group_by_max_weight/) | 16.0.1.0.0 |  | Allows to filter available pickings for which a maximum weight is not exceeded.
[stock_picking_invoice_link](stock_picking_invoice_link/) | 16.0.1.0.1 |  | Adds link between pickings and invoices
[stock_picking_purchase_order_link](stock_picking_purchase_order_link/) | 16.0.1.0.1 |  | Link between picking and purchase order
[stock_picking_sale_order_link](stock_picking_sale_order_link/) | 16.0.1.0.0 |  | Link between picking and sale order
[stock_picking_show_return](stock_picking_show_return/) | 16.0.1.0.1 |  | Show returns on stock pickings
[stock_picking_start](stock_picking_start/) | 16.0.1.0.3 |  | Add button to start picking
[stock_procurement_customer](stock_procurement_customer/) | 16.0.1.0.0 |  | Allows to store customer if different from the partner
[stock_putaway_hook](stock_putaway_hook/) | 16.0.1.0.0 |  | Add hooks allowing modules to add more putaway strategies
[stock_quant_package_dimension](stock_quant_package_dimension/) | 16.0.1.0.0 |  | Use dimensions on packages
[stock_quant_package_product_packaging](stock_quant_package_product_packaging/) | 16.0.1.0.1 |  | Use product packagings on packages
[stock_receipt_lot_info](stock_receipt_lot_info/) | 16.0.1.0.0 |  | Be able to introduce more info on lot/serial number while processing a receipt.
[stock_restrict_lot](stock_restrict_lot/) | 16.0.1.1.0 | [![florian-dacosta](https://github.com/florian-dacosta.png?size=30px)](https://github.com/florian-dacosta) | Base module that add back the concept of restrict lot on stock move
[stock_split_picking](stock_split_picking/) | 16.0.1.0.2 |  | Split a picking in two not transferred pickings

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Odoo Community Association (OCA)
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit
organization whose mission is to support the collaborative development of Odoo features
and promote its widespread use.
