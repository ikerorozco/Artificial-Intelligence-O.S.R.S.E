import os
import requests
import xml.etree.ElementTree as ET
from fpdf import FPDF
import argparse

# Configuración de GROBID
GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

# Configuración de argumentos de línea de comandos
parser = argparse.ArgumentParser(description="Extrae enlaces de referencias en PDFs usando GROBID y genera un PDF de salida.")
parser.add_argument("-i", "--input", default="data", help="Carpeta donde están los archivos PDF (por defecto 'pdfs').")
parser.add_argument("-o", "--output", default="Enlaces_Extraidos.pdf", help="Nombre del PDF de salida.")

args = parser.parse_args()
PDF_DIRECTORY = args.input
OUTPUT_PDF = os.path.join(PDF_DIRECTORY, args.output)

# Verifica que la carpeta existe
if not os.path.exists(PDF_DIRECTORY):
    print(f" La carpeta '{PDF_DIRECTORY}' no existe.")
    exit(1)

# Lista automática de PDFs en la carpeta
pdf_files = [f for f in os.listdir(PDF_DIRECTORY) if f.endswith(".pdf")]

if not pdf_files:
    print(" No hay archivos PDF en la carpeta.")
    exit(1)

# Función para extraer enlaces desde las referencias del XML de GROBID
def extract_reference_links(xml_text):
    try:
        root = ET.fromstring(xml_text)
        namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}
        
        references = root.findall(".//tei:biblStruct", namespaces)
        links = [ref.find(".//tei:ptr", namespaces).attrib['target'] for ref in references if ref.find(".//tei:ptr", namespaces) is not None]
        return links
    except ET.ParseError:
        return []

# Inicializar el documento PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Lista de Enlaces Extraídos", ln=True, align="C")
pdf.ln(10)  # Espacio

# Procesar cada PDF en la carpeta
all_links = {}

for pdf_name in pdf_files:
    pdf_path = os.path.join(PDF_DIRECTORY, pdf_name)
    print(f" Procesando: {pdf_name}")
    
    try:
        with open(pdf_path, "rb") as pdf_file:
            response = requests.post(GROBID_URL, files={"input": pdf_file}, data={"consolidate": "1"})
        
        if response.status_code == 200:
            links = extract_reference_links(response.text)
            all_links[pdf_name] = links  # Guardar en el diccionario

            if links:
                print(f" Links encontrados en '{pdf_name}': {len(links)} enlaces.")
            else:
                print(f" No se encontraron links en '{pdf_name}'.")
        else:
            print(f" Error procesando '{pdf_name}': Código {response.status_code}")
    except FileNotFoundError:
        print(f" El archivo '{pdf_name}' no se encontró.")

# Agregar enlaces al PDF
for pdf_name, links in all_links.items():
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, pdf_name, ln=True, align="L")
    pdf.set_font("Arial", "", 10)
    
    if links:
        for link in links:
            pdf.multi_cell(0, 5, link)
    else:
        pdf.cell(0, 5, "No se encontraron enlaces.", ln=True)

    pdf.ln(5)  # Espaciado entre documentos

# Guardar el PDF con la lista de enlaces
pdf.output(OUTPUT_PDF)
print(f"\n El archivo con los enlaces extraídos se ha guardado en: {OUTPUT_PDF}")
