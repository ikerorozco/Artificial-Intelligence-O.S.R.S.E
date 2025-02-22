import requests
import xml.etree.ElementTree as ET
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter
import re

# Ruta del servidor GROBID
GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

# Ruta del PDF a procesar (Este es un ejemplo y puede ser modificado en cualquier momento)
# para que funcione debera de tener el nombre especifico del pdf y la terminacion .pdf 
# "Ejemplo.pdf" 
pdf_path = "Boosting Data.pdf"

# Función para extraer el texto del <abstract> en el XML de GROBID
def extract_abstract(xml_text):
    try:
        # Definir namespace de TEI
        namespaces = {"tei": "http://www.tei-c.org/ns/1.0"}

        root = ET.fromstring(xml_text)
        # Buscar el abstract con el namespace TEI
        abstract = root.find(".//tei:abstract", namespaces)

        if abstract is not None:
            # Extraer los párrafos dentro del abstract
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

# Enviar PDF a GROBID
with open(pdf_path, "rb") as pdf_file:
    files = {"input": pdf_file}
    response = requests.post(GROBID_URL, files=files, data={"consolidate": "1"})

# Procesar respuesta XML
if response.status_code == 200:
    abstract_text = extract_abstract(response.text)
    
    if abstract_text:
        print("Abstract extraído:", abstract_text[:500])  # Muestra los primeros 500 caracteres

        # Procesar texto y generar nube de palabras basada en frecuencia
        word_frequencies = process_text(abstract_text)

        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color="white",
            colormap="viridis",  # Mejor contraste
            max_words=100
        ).generate_from_frequencies(word_frequencies)

        # Mostrar la nube de palabras
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
    else:
        print("No se encontró un abstract en el documento.")
else:
    print(f"Error en la solicitud a GROBID: {response.status_code}")
