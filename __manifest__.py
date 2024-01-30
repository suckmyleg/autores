# -*- coding: utf-8 -*-
{
    'name': "Autores",  
    'summary': "Gestión de autores", 
    'description': """
                    Gestor de Autores
                    ==============
                    """,  
    'application': True,
    'author': "Autor",
    'website': "website",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv'
    ],
}
