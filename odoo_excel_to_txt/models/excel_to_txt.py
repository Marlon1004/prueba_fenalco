def convert_to_txt(self):
    """ Convierte un archivo Excel en un archivo TXT y lo descarga """
    if not self.file:
        return

    # Decodificar archivo
    file_content = base64.b64decode(self.file)
    
    # Leer el archivo Excel
    workbook = xlrd.open_workbook(file_contents=file_content)
    sheet = workbook.sheet_by_index(0)  # Tomar la primera hoja

    # Convertir el contenido en texto
    txt_content = ""
    for row_idx in range(sheet.nrows):
        row_values = [str(sheet.cell_value(row_idx, col_idx)) for col_idx in range(sheet.ncols)]
        txt_content += ",".join(row_values) + "\n"

    # Codificar el TXT en base para su descarga en Odoo
    txt_encoded = base64.b64encode(txt_content.encode('utf-8'))

    # Crear el archivo adjunto en Odoo
    attachment = self.env['ir.attachment'].create({
        'name': self.file_name.replace('.xls', '.txt').replace('.xlsx', '.txt'),
        'type': 'binary',
        'datas': txt_encoded,
        'res_model': 'excel.to.txt',
        'res_id': self.id,
    })

    return {
        'type': 'ir.actions.act_url',
        'url': f'/web/content/{attachment.id}?download=true',
        'target': 'new',
    }
