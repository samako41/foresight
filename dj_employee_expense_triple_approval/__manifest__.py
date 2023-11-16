
{
    'name': 'HR Employee Expense Triple Approval in Odoo',
    'version': '16.0.0.0',
    'category': 'Human Resources',
    'summary': 'Hr Employee Expense Double Approval Employee Expense Tripple Approval Request Employee Expense approval mail notification hr expense approval expense triple validation approval employee expense approve expense second approval hr expense multi approval',
    'description': """This app allows your employees to create request for expenses. This app will work with multi currency.
	
	    employee Expense Triple Approval Request in odoo,
        employee Expense Request in odoo,
        Expenses/Expense Request in odoo,
        Expense request send with mail in odoo,
        Expense request approval with mail in odoo,
        Expenses/Expense Request to Approve,
        Expenses/Expense Request to Pay,
        employee Expense Multiple Request,
        Expense Request Approve by HR Manager,
        Expense Request Approve by Expense Manager,
        Integrated with Expense and Accounting Entry,
        Print Expense in odoo,
	
	
	 """,
    
	
	
	'author': 'BrowseInfo',
    "price": 9,
    "currency": 'EUR',
    'website': 'https://www.browseinfo.in',
    'depends': ['dj_employee_expense_double_approval'],
    'data': [
            'views/hr_approve.xml',
            'security/security.xml',
            'views/mail_template.xml',
    ],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': True,
    'live_test_url': 'https://youtu.be/wDRvsuvKR58',
    "images":['static/description/Banner.gif'],
}
