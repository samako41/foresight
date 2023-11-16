odoo.define('pos_print_kitchen_receipt.PrintkitchenReceiptButton', function (require) {
    "use strict";

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require("@web/core/utils/hooks");
    const Registries = require('point_of_sale.Registries');


    var core = require('web.core');
	var _t = core._t;

    class PrintkitchenReceiptButton extends PosComponent {
        setup() {
            super.setup();
            useListener('click', this.onClick);
        }
        get currentOrder(){
            return this.env.pos.get_order();
        }
        async onClick() {
            var selected_orderline = this.currentOrder.get_selected_orderline();            
            if(typeof(selected_orderline) === 'object'){
                this.showScreen(this.nextScreen);
            }
            else{
                this.showPopup('ErrorPopup', {
                    title: this.env._t('No Product  Selected'),
                    body: this.env._t('You must first choose a product.'),
                });
            }

        }
        get nextScreen() {
            return 'PrintKitchenReceiptScreen';
        }
    }
    PrintkitchenReceiptButton.template = 'PrintkitchenReceiptButton';
    ProductScreen.addControlButton({
        component: PrintkitchenReceiptButton,
        condition: function() {
            return this.env.pos.config.print_kitchen_receipt;            
        },
        position: ['before', 'SetFiscalPositionButton'],
    });

    Registries.Component.add(PrintkitchenReceiptButton);
    return PrintkitchenReceiptButton;
});