# © 2023 FactorLibre - Alejandro Ji Cheung <alejandro.jicheung@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Multi-Company: Default Configuration",
    "version": "16.0.1.0.0",
    "category": "Other",
    "author": "FactorLibre",
    "website": "https://github.com/OCA/multi-company",
    "license": "LGPL-3",
    "summary": "",
    "depends": [
        "product_company_default",
        "partner_company_default",
    ],
    "data": [
        "views/res_config_settings_view.xml",
        "data/multicompany_default_configuration_data.xml",
    ],
    "installable": True,
    "application": False,
}
