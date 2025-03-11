from odoo import models, fields, api

class ExcelToTxt(models.Model):
    _name = 'excel.to.txt'
    _description = 'Módulo para conversión de Excel a TXT'

    name = fields.Char(string='Nombre', required=True)
    file = fields.Binary(string='Archivo Excel', required=True)
    file_name = fields.Char(string='Nombre del archivo')

    def convert_to_txt(self):
        # Lógica para convertir Excel a TXT
        pass
