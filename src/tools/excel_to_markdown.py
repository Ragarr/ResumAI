import pandas as pd
import sys

def excel_to_markdown(excel_file, output_md=None):
    # Cargar el archivo Excel
    xls = pd.ExcelFile(excel_file)
    
    

    # Nombre del archivo sin la extensión
    file_name = excel_file.split('/')[-1]
    
    # Inicializar el contenido del archivo Markdown
    md_content = f"# {file_name}\n\n"
    
    for sheet_name in xls.sheet_names:
        # Leer cada hoja en un DataFrame
        df = pd.read_excel(xls, sheet_name=sheet_name)
        
        # Convertir el DataFrame a una tabla Markdown
        md_table = df.to_markdown(index=False)
        
        # Agregar la tabla al contenido
        md_content += f"## {sheet_name}\n\n{md_table}\n\n"
    
    if output_md is None:
        # return the markdown content if no output file is specified
        return md_content

    # Escribir a un archivo Markdown
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(md_content)
    
    print(f"Archivo Markdown generado: {output_md}")

# Uso del script
def main():
    if len(sys.argv) < 3:
        print("Uso: python script.py <archivo_excel> <archivo_markdown>")
        sys.exit(1)
    
    excel_file = sys.argv[1]
    output_md = sys.argv[2]
    
    excel_to_markdown(excel_file, output_md)

if __name__ == "__main__":
    main()
