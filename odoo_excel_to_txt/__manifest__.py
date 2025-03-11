{
    'name': 'Excel to TXT Converter',
    'version': '16.0.1.0.0',
    'summary': 'Convierte archivos Excel a TXT',
    'category': 'Tools',
    'author': 'Tu Nombre',
    'website': 'https://github.com/TuUsuario',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/excel_to_txt_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}