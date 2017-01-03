# -*- coding: utf-8 -*-
# © 2013-Today Odoo SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Inter Company Module for Invoices',
    'summary': 'Intercompany INV rules',
    'version': '8.0.1.0.0',
    'category': 'Accounting & Finance',
    'website': 'http://www.odoo.com',
    'author': 'Odoo SA, Akretion, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'account',
    ],
    'data': [
        'views/res_company_view.xml',
        'views/res_config_view.xml',
        'config.yml'
    ],
    'demo': [
        'demo/inter_company_invoice.xml',
    ],
}
