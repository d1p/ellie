# -*- coding: utf-8 -*-
# Copyright 2016 Openworx, LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Ellie: Backend theme",
    "summary": "Odoo 10.0 Private theme",
    "version": "1.0",
    "category": "Themes/Backend",
    "website": "https://nihan.me",
	"description": """
		Backend theme for odoo
    """,
	'images':[
        'images/screen.png'
	],
    "author": "d1p",
    "license": "Private",
    "installable": True,
    "depends": [
        'web',
    ],
    "data": [
        'views/assets.xml',
        'views/web.xml',
    ],
}

