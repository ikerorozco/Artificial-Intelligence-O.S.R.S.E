import os
import requests
import xml.etree.ElementTree as ET
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter
import re
import argparse

# Configuración de GROBID
GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

# Configuración de argumentos de línea de comandos
parser = argparse.ArgumentParser(description="Extrae el abstract de PDFs usando GROBID y genera una nube de palabras.")
parser.add_argument("-i", "--input", default="data", help="Carpeta donde están los archivos PDF (por defecto 'pdfs').")

args = parser.parse_args()
PDF_DIRECTORY = args.input

# Verifica que la carpeta existe
if not os.path.exists(PDF_DIRECTORY):
    print(f" La carpeta '{PDF_DIRECTORY}' no existe.")
    exit(1)

# Verifica que haya PDFs en la carpeta
pdf_files = [f for f in os.listdir(PDF_DIRECTORY) if f.endswith(".pdf")]

if not pdf_files:
    print(" No hay archivos PDF en la carpeta.")
    exit(1)

# Namespace de TEI (para buscar etiquetas correctamente)
namespaces = {"tei": "http://www.tei-c.org/ns/1.0"}

# Función para extraer el texto del <abstract> en el XML de GROBID
def extract_abstract(xml_text):
    try:
        root = ET.fromstring(xml_text)
        abstract = root.find(".//tei:abstract", namespaces)

        if abstract is not None:
            paragraphs = abstract.findall(".//tei:p", namespaces)
            text = " ".join(p.text for p in paragraphs if p.text)  # Une los textos de <p>
            return text.strip() if text else None  # Devuelve None si está vacío
        return None
    except ET.ParseError:
        return None

# Función para limpiar texto y contar palabras clave
def process_text(text):
    text = text.lower()  # Convertir a minúsculas
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Quitar signos de puntuación y números
    words = text.split()
    
    # Stopwords ampliadas (añadir más si es necesario)
    stopwords = set(STOPWORDS).union({"et", "al", "using", "based", "also", "show", "however", "approach"})
    
    # Filtrar palabras relevantes
    filtered_words = [word for word in words if word not in stopwords and len(word) > 2]
    
    return Counter(filtered_words)  # Cuenta la frecuencia de palabras

# Procesar cada PDF en la carpeta
for pdf in pdf_files:
    pdf_path = os.path.join(PDF_DIRECTORY, pdf)
    print(f" Procesando: {pdf}")

    with open(pdf_path, "rb") as pdf_file:
        response = requests.post(GROBID_URL, files={"input": pdf_file}, data={"consolidate": "1"})

    if response.status_code == 200:
        abstract_text = extract_abstract(response.text)

        if abstract_text:
            print(f" Abstract extraído de {pdf}: {abstract_text[:200]}...")  # Muestra un fragmento
            
            # Procesar texto y generar nube de palabras
            word_frequencies = process_text(abstract_text)
            wordcloud = WordCloud(
                width=800, height=400, background_color="white",
                colormap="viridis", max_words=100
            ).generate_from_frequencies(word_frequencies)

            # Mostrar la nube de palabras
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.title(f"Nube de palabras - {pdf}")
            plt.show()
        else:
            print(f" No se encontró un abstract en {pdf}.")
    else:
        print(f" Error procesando {pdf}: Código {response.status_code}")