{
    'name': 'Rebate for new customers',
    'summary': '''
        Adds an "apply discount" button to a sales order if a customer has never
        purchased a motorcycle from them before. When clicked, it will add a
        pricelist that removes $2500 from the total price
    ''',
    "author": "Odoo, Inc.",
    "website": "www.odoo.com",
    'license': 'OPL-1',
    'depends': [
        'motorcycle_registry',
        'sale_management'
        ],
    'data': [
        'data/pricelist_data.xml',
        'views/sale_views.xml'
    ],
    'category': 'Kawiil/Registry',
    'auto_install': True,
}