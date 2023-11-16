odoo.define('pos_print_kitchen_receipt.PrintKitchenReceiptScreen', function (require) {
    'use strict';

    // const { Printer } = require('point_of_sale.Printer');
    // const { is_email } = require('web.utils');
    // const { useRef, useContext } = owl.hooks;
    const { useErrorHandlers, onChangeOrder } = require('point_of_sale.custom_hooks');
    const Registries = require('point_of_sale.Registries');
    const AbstractReceiptScreen = require('point_of_sale.AbstractReceiptScreen');

    const { onMounted, useRef, status } = owl;

    const PrintKitchenReceiptScreen = (AbstractReceiptScreen) => {
        class PrintKitchenReceiptScreen extends AbstractReceiptScreen {

            setup() {
                super.setup();
                useErrorHandlers();
                this.kitchenOrderReceipt = useRef('kitchen-order-receipt');
                const order = this.currentOrder;
                onMounted(this.onMounted);
            }

            onMounted() {
                setTimeout(async () => {
                    if (status(this) === "mounted") {  
                        if (this.kitchenOrderReceipt.el != null){
                            let images = this.kitchenOrderReceipt.el.getElementsByTagName('img');                        
                            for (let image of images) {
                                await image.decode();
                            }
                        }
                    }
                }, 0);
            }

            get currentOrder() {
                return this.env.pos.get_order();
            }

            async printReceipt() {
                const isPrinted = await this._printReceipt();
                if (isPrinted) {                    
                    this.currentOrder._kitchen_receipt_printed = true;
                }
            }
        }

        PrintKitchenReceiptScreen.template = 'PrintKitchenReceiptScreen';
        return PrintKitchenReceiptScreen;
    }
    Registries.Component.addByExtending(PrintKitchenReceiptScreen, AbstractReceiptScreen);

    return PrintKitchenReceiptScreen;
});