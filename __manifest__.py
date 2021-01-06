# -*- coding: utf-8 -*-

{
    'name': 'INVERAGRO Sales & CRM',
    'version': '1.0',
    'category': 'Sales/CRM',
    'sequence': 5,
    'summary': 'Track leads and close opportunities',
    'description': "",
    'depends': [
        'crm', 
        'sale_management', 
        'website_sale',
    ],
    'data': [
        'views/sale_order.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
