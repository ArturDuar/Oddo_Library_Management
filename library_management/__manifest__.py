{
    'name': 'Library Management',
    'version': '1.0',
    'author': 'Arturo',
    'category': 'Administration',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/socio_views.xml',
        'views/libro_views.xml',
        'views/menu_views.xml',     
    ],
    'installable': True,
    'application': True,
}