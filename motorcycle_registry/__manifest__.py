{
    "name": "Motorcycle Registry",
    "summary": "Manage Registration of Motorcycles", 
    "description": """
    Motorcycle Registry
====================
This Module is used to keep track of the Motorcycle Reistration and Ownership of each motorcycled of the brand.
    """,
    "version": "0.1",
    "category": "Kawiil/Registry",
    "license": "OPL-1",
    "depends": ["base"], 
    "data": [
        "security/registry_groups.xml",
        "security/ir.model.access.csv",
        'data/registry_data.xml',
        "views/motorcycle_registry_menuitems.xml",
        "views/motorcycle_registry_views.xml",
    ],
    "demo": [
        "demo/motorcycle_registry_demo.xml",
    ],
    "author": "Odoo, Inc.",
    "website": "www.odoo.com",
    "application": True,
    
}

#
#My version, not working
#{
#    'name': 'Motorcycle Registry',
#    'summary': 'Manage Registration of Motorcycles',
#    'description': 'Motorcycle Registry',
#    'author': 'akendall-hightower',
#    'version': '0.0.1',
#    'category': 'Kawii/Custom Modules',
#    "license": "OPL-1",
#    'website': 'https://github.com/akendall-hightower/odoo-dev',
#    'depends': ['base'],
#    'data': [
#        "security/registry_groups.xml",
#        "security/ir.model.access.csv",
#        'data/data.xml'
#    ],
#    'demo': [
#        'data/demo.xml'
#    ],
#    'assets': [],
#    'application': True,
#}
