============================
Paystack Payment for odoo
============================

Installation
------------

This addon can be installed as any other regular Odoo addon:

- Unzip the addon in one of Odoo's addons paths.
- Login to Odoo as a user with administrative privileges, go into debug mode.
- Go to *Apps -> Update Apps List*, click *Update* in the dialog window.
- Go to *Apps -> Apps*, remove the *Apps* filter in the search bar and search
  for *Paystack Payment Acquirer*. Click *Install* button on the addon.


.. note:: You you would like to use the payment acquirer in the eCommerce shop,
    make sure the *eCommerce* module (*website_sale*) is installed as well.

Configuration
-------------

Before configuring the Paystack payment acquirer, register an account on
 `paystack.com`_ for a test account and login.

Once you have logged in, click on the settings menu at the bottom left
corner of the page and select *API*.

.. image:: api_settings.png
    :alt: API Settings page.
    :class: img-responsive img-thumbnail

In this window:

- Copy the values in your Public key .
- Copy the values in your Secret key.
.

.. note:: Use the credentials on the live mode to test on odoo production servers 
and use the credentials on the test mode to test on Odoo test servers.


Now, let's configure the payment acquirer:

- Login to Odoo as a user with administrative privileges, go into debug mode.
- Go to *Website -> Configuration -> eCommerce -> Payment Acquirers* or
  *Invoicing -> Configuration -> Payments -> Payment Acquirers* and click
  *Configure* on the *Paystack* acquirer.

- In the *Credentials* tab, enter the Public and Secret key from Rave 
  *API credentials* section noted earlier:


- Click on the *Save* button.
- Click on the *Publish* button to make the acquirer available for you in the
  eCommerce shop.

