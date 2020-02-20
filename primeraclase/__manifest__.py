# -*- coding: utf-8 -*-
{
    'name': "primeraclase",

    'summary': """
        Esta es la primera clase de desarrollo """,

    'description': """
        Esta es la primera clase de desarrollo de primera generacion de Todooers
    """,

    'author': "Todoo SAS",
    'website': "http://www.todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'todoo',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
