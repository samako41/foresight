odoo.define('pos_print_kitchen_receipt.KitchenReceipt', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    const { onWillUpdateProps } = owl;

    class KitchenReceipt extends PosComponent {
        setup() {
            super.setup();
            this._receiptEnv = this.props.order.getOrderReceiptEnv();

            onWillUpdateProps((nextProps) => {
                this._receiptEnv = nextProps.order.getOrderReceiptEnv();
            });
        }
        get receipt() {
            return this.receiptEnv.receipt;
        }
        get orderlines() {
            return this.receiptEnv.orderlines;
        }
        get receiptEnv () {
          return this._receiptEnv;
        }
    }
    KitchenReceipt.template = 'KitchenReceipt';

    Registries.Component.add(KitchenReceipt);

    return KitchenReceipt;
});