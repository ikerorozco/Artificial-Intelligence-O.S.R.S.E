import os
import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import argparse

# Configuración de GROBID
GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

# Configuración de argumentos de línea de comandos
parser = argparse.ArgumentParser(description="Extrae el abstract de PDFs usando GROBID y genera una grafica de barras.")
parser.add_argument("-i", "--input", default="data", help="Carpeta donde están los archivos PDF (por defecto 'pdfs').")

args = parser.parse_args()
PDF_DIRECTORY = args.input

# Verifica que la carpeta existe
if not os.path.exists(PDF_DIRECTORY):
    print(f"La carpeta '{PDF_DIRECTORY}' no existe.")
    exit(1)

# Verifica que haya PDFs en la carpeta
pdf_files = [f for f in os.listdir(PDF_DIRECTORY) if f.endswith(".pdf")]

if not pdf_files:
    print(" No hay archivos PDF en la carpeta.")
    exit(1)

# Namespace de TEI (para buscar etiquetas correctamente)
namespaces = {"tei": "http://www.tei-c.org/ns/1.0"}

# Función para contar figuras en el XML de GROBID
def count_figures(xml_text):
    try:
        root = ET.fromstring(xml_text)
        figures = root.findall(".//tei:figure", namespaces)
        return len(figures)
    except ET.ParseError:
        return 0

# Diccionario para almacenar el número de figuras detectadas por cada PDF
figures_count = {}

# Procesar cada PDF en la carpeta
for pdf in pdf_files:
    pdf_path = os.path.join(PDF_DIRECTORY, pdf)
    print(f" Procesando: {pdf}")

    with open(pdf_path, "rb") as pdf_file:
        response = requests.post(GROBID_URL, files={"input": pdf_file}, data={"consolidate": "1"})

    if response.status_code == 200:
        num_figures = count_figures(response.text)
        figures_count[pdf] = num_figures
        print(f" {pdf}: {num_figures} figuras encontradas.")
    else:
        print(f" Error procesando {pdf}: Código {response.status_code}")
        figures_count[pdf] = 0

# Verifica si se encontraron figuras antes de generar la gráfica
if not any(figures_count.values()):
    print("No se encontraron figuras en ningún archivo PDF.")
    exit(1)

# Crear gráfica de barras
plt.figure(figsize=(10, 6))
plt.bar(figures_count.keys(), figures_count.values(), color="skyblue")
plt.xlabel("Archivos PDF")
plt.ylabel("Número de Figuras")
plt.title("Cantidad de Figuras en los PDFs")
plt.xticks(rotation=45, ha="right")  # Ajusta la rotación de etiquetas para mejor visualización
plt.tight_layout()  # Evita que se corten las etiquetas
plt.show()