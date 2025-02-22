import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Configuración de GROBID mediante el api usando processFulltextDocument y localhost 8070
GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

# Lista de PDFs a procesar (Estos son ejemplos y pueden ser modificados en cualquier momento)
# para que funcionen deberan de tener el nombre especifico del pdf y la terminacion .pdf 
# Ejemplo.pdf

pdf_files = [
    "Machine Learning California.pdf",
    "Models Efficiency.pdf",    
    "Multitasking Learning.pdf",
    "neural networks.pdf",
    "Hierarchicaal Learning.pdf",
    "Hypergraphs.pdf",
    "Landscape analysis.pdf",
    "Paradox.pdf", 
    "Privacy Amplification.pdf",
    "Boosting Data.pdf"
]

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

# Procesar cada PDF

# Diccionario para almacenar el número de figuras detectadas en cada PDF
figures_count = {}

# Itera sobre la lista de archivos PDF a procesar
for pdf_path in pdf_files:
    pdf_name = pdf_path.split("\\")[-1]  # Extrae solamente el nombre del archivo

    with open(pdf_path, "rb") as pdf_file: # abre el archivo pdf
        # Envía una solicitud POST al servidor de Grobid para procesar el PDF
        response = requests.post(GROBID_URL, files={"input": pdf_file}, data={"consolidate": "1"})

    # Verifica si la respuesta del servidor es exitosa (código 200)
    if response.status_code == 200:
        # Llama a la función count_figures para contar el número de figuras en el resultado
        num_figures = count_figures(response.text)
        figures_count[pdf_name] = num_figures
        print(f"{pdf_name}: {num_figures} figuras encontradas.")
    else:
        print(f"Error procesando {pdf_name}: Código {response.status_code}")
        figures_count[pdf_name] = 0

# Crear gráfica de barras
plt.figure(figsize=(10, 6))
plt.bar(figures_count.keys(), figures_count.values(), color="skyblue")
plt.xlabel("Archivos PDF")
plt.ylabel("Número de Figuras")
plt.title("Cantidad de Figuras en cada PDF (GROBID)")
plt.xticks(rotation=45)
plt.show()
