# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Whatsapp',
    'version': '16.0.1.0.0',
    'sequence': 10,
    'category': 'Extra Tools',
    'summary': """
        Odoo Whatsapp Redirect
    """,
    'description': "Whatsapp Redirect",
    'author': 'Abdalrahman Shahrour',
    'maintainer': 'Abdalrahman Shahrour',
    'website': 'https://www.linkedin.com/in/shahrour/',
    'license': 'LGPL-3',

    'depends': [
        'base',
        'web',
        'mail'
    ],
    'data': [
    ],
    'assets': {
        'mail.assets_discuss_public': [
            'odoo_whatsapp_redirect/static/src/components/wa_button/*',
        ],
        'web.assets_backend': [
            'odoo_whatsapp_redirect/static/src/components/*/*',
        ],
    },
    'demo': [],
    'installable': True,
    'auto_install': False,
}
