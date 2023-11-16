odoo.define('product_price_checker.product_price_checker', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var QWeb = core.qweb;

    setInterval(function(){ self.$(".checker_input").change() }, 1800);

    var product_price_checker = AbstractAction.extend({
        contentTemplate: "ProductPriceChecker",
        events: {
            'click .checker_button_0': function() { 
                this.$('.checker_input').val(this.$('.checker_input').val() + 0); 
            },
            'click .checker_button_1': function() { 
                this.$('.checker_input').val(this.$('.checker_input').val() + 1); 
            },
            'click .checker_button_2': function() { 
                this.$('.checker_input').val(this.$('.checker_input').val() + 2); 
            },
            'click .checker_button_3': function() { 
                this.$('.checker_input').val(this.$('.checker_input').val() + 3); 
            },
            'click .checker_button_4': function() { 
                this.$('.checker_input').val(this.$('.checker_input').val() + 4); 
            },
            'click .checker_button_5': function() { 
                this.$('.checker_input').val(this.$('.checker_input').val() + 5); 
            },
            'click .checker_button_6': function() { 
                this.$('.checker_input').val(this.$('.checker_input').val() + 6); 
            },
            'click .checker_button_7': function() { 
                this.$('.checker_input').val(this.$('.checker_input').val() + 7); 
            },
            'click .checker_button_8': function() { 
                this.$('.checker_input').val(this.$('.checker_input').val() + 8); 
            },
            'click .checker_button_9': function() { 
                this.$('.checker_input').val(this.$('.checker_input').val() + 9);
            },
            'click .checker_button_b': function() { 
                var value = this.$('.checker_input').val();
                if (value){
                    this.$('.checker_input').val(value.substr(0, value.length - 1));
                }
                this.start_focus();
            },
            'click .checker_button_c': function() {
                this.$('.checker_input').val(''); 
                this.render_html(false,'');
                this.start_focus();
            },
            'click .checker_button_k': function() {
               this.get_product_details();
            },
            'change input.checker_input': function(){
                this.get_product_details();
            },
        },
        start: function () {
            var self = this;
            self.start_clock();
            self.start_focus();
            return this._super.apply(this, arguments);
        },
        start_clock: function () {
            var self = this;
            this.clock_start = setInterval(function() {
                self.$(".checker_clock").text(new Date().toLocaleTimeString(navigator.language, {hour: '2-digit', minute:'2-digit', second:'2-digit'}));
            }, 500);
            this.$(".checker_clock").show().text(new Date().toLocaleTimeString(navigator.language, {hour: '2-digit', minute:'2-digit', second:'2-digit'}));
        },
        start_focus: function(){
            var self = this;
            setTimeout(function(){
                const input = self.$('.checker_input');
                const originalValue = input.val();
                input.val('');
                input.blur().focus().val(originalValue);
            }, 500);
            self.$(".checker_input").focus();
        },
        destroy: function () {
            clearInterval(this.clock_start);
            this._super.apply(this, arguments);
        },

        get_product_details: function(){
            var self = this;
            var val = self.$('.checker_input').val();
            if(val != ""){
                self._rpc({
                    model: 'product.product',
                    method: 'get_product_details',
                    args: [val],
                }).then(function (product){
                    self.render_html(product, val);
                });
            }
        },
        render_html: function(product, val){
            var self = this;
            if(product && product['product_id'] !=false ){
                self.product_id=product['product_id'];
                self.product_name=product['product_name'];
                self.product_description_sale=product['product_description_sale'];
                self.product_price=product['product_price'];
                self.product_price_tax=product['product_price_tax'];
                self.product_barcode=product['product_barcode'];
                self.product_code=product['product_code'];
                self.product_currency_id=product['product_currency_id'];
                self.product_uom_id=product['product_uom_id'];
                self.checker_input= "";
                self.$el.html(QWeb.render("ProductPriceChecker", {widget: self}));                
            }
            else{
                self.product_id="";
                self.product_name="";
                self.product_description_sale="";
                self.product_price="";
                self.product_price_tax="";
                self.product_barcode="";
                self.product_code= "";
                self.product_currency_id="";
                self.product_uom_id="";
                self.checker_input= val;
                self.$el.html(QWeb.render("ProductPriceChecker", {widget: self}));
            }
            setTimeout(function(){
                const input = self.$('.checker_input');
                const originalValue = input.val();
                input.val('');
                input.blur().focus().val(originalValue);
            }, 0);
            
        }
    });

    core.action_registry.add('product_price_checker', product_price_checker);
    return product_price_checker;

});
