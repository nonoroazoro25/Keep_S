# -*- coding: utf-8 -*-
{
    'name': "体重管理",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        记录体重
    """,

    'author': "Ssha",
    'website': "http://www.yourcompany.com",

    'category': 'self-Management/Weight',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/diet_record.xml',
        'views/weight_record.xml',
        'views/heat_query.xml',
        'views/menu.xml',
    ],
    'qweb': [
        'static/src/xml/custom_user_tree.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
