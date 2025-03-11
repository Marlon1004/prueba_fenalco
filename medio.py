

# segun mi experiencia es adecuado utilizar pandas

import sys
import pandas as pd

def transformar_datos(excel_path, output_txt):
    try:
        # Leer el archivo Excel
        df = pd.read_excel(excel_path, dtype=str).fillna('')  # Reemplaza NaN con cadena vacía
        
        # Aplicar reglas de transformación
        if 'ANIO' in df.columns:
            df['ANIO'] = df['ANIO'].apply(lambda x: str(x).zfill(4) if str(x).isdigit() else x)
        
        if 'CONCEPTO' in df.columns:
            df['CONCEPTO'] = df['CONCEPTO'].apply(lambda x: str(x).ljust(10, '$') if isinstance(x, str) and len(x) < 10 else x)
        
        if 'VALOR' in df.columns:
            df['VALOR'] = df['VALOR'].apply(lambda x: str(x).zfill(20) if str(x).isdigit() else x)

        # Dejar valores que no cumplan reglas tal como están
        df = df.fillna('')  # Asegurar que todos los NaN se conviertan en cadena vacía
        
        # Convertir todo a una sola cadena sin espacios extra
        contenido_txt = df.apply(lambda row: ''.join(row.astype(str)), axis=1).to_string(index=False, header=False)

        # Escribir al archivo de salida
        with open(output_txt, 'w', encoding='utf-8') as f:
            f.write(contenido_txt + '\n')

        print(f"✅ Archivo generado correctamente: {output_txt}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python medio.py <ruta_del_excel> <ruta_salida_txt>")
    else:
        excel_path = sys.argv[1]
        output_txt = sys.argv[2]
        transformar_datos(excel_path, output_txt)
