odoo.define('pos_product_qty_zero_order.ProductScreen', function (require) {
    'use strict';

    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    var rpc = require('web.rpc');

    const { _t } = require('web.core');

    const PWPOSWaiter = (ProductScreen) =>
        class extends ProductScreen {
            _onClickPay() {
                var self = this;
                var order = this.env.pos.get_order();
                var orderlines = order.get_orderlines();
                let product_list = []
                var returnLines = orderlines.filter((line) => line.quantity == 0);
                returnLines.forEach(function(line) {
                    product_list.push(line.product.display_name)
                });
                if(this.env.pos.config.pw_not_zero_qty && returnLines.length > 0){
                    this.showPopup('ErrorPopup', {
                        title: this.env._t('Zero Quantity not Allowed'),
                        body: this.env._t(product_list),
                    });
                    return false
                }
                else {
                    super._onClickPay()
                }
            }
        };

    Registries.Component.extend(ProductScreen, PWPOSWaiter);

    return ProductScreen;
});
