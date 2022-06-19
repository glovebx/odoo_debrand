# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Debrand',
    'category': 'Cryptocurrency',
    'summary': 'Debrand for redistribution',
    'version': '1.0',
    'description': """
        This module debrand original verbose brand information
        """,
    'depends': [ ],
    'data': [
        'views/views.xml'
    ],
    'assets': {
        'web.assets_qweb': [
        ],
        'web.assets_backend': [
            'debrand/static/src/**/*',
        ],
        'web.assets_frontend': [
            'debrand/static/src/css/web_no_bubble.scss',
        ],
        'web.tests_assets': [
        ],
        'web.qunit_mobile_suite_tests': [
        ],
    },
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
}
