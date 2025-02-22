import requests
import xml.etree.ElementTree as ET

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

# Función para extraer enlaces desde las referencias del XML de GROBID
def extract_reference_links(xml_text):
    try:
        # Convierte el texto XML en un árbol de elementos
        root = ET.fromstring(xml_text)
        namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}  # Espacio de nombres TEI
        
        # Encuentra todas las referencias bibliográficas en <biblStruct>
        references = root.findall(".//tei:biblStruct", namespaces)
        
        # Lista para almacenar los enlaces extraídos
        links = []
        # Itera sobre todas las referencias encontradas
        for ref in references:
            ptr = ref.find(".//tei:ptr", namespaces)  # Busca la etiqueta <ptr>
            # Si la etiqueta <ptr> existe y tiene un atributo 'target', extrae el enlace
            if ptr is not None and 'target' in ptr.attrib:
                links.append(ptr.attrib['target'])  # Extrae la URL
        # Devuelve la lista de enlaces encontrados
        return links
    except ET.ParseError:
        return []

# Procesar cada PDF
for pdf_path in pdf_files:
    print(f"\nProcesando: {pdf_path}")

    try:
        with open(pdf_path, "rb") as pdf_file:#abre el archivo pdf
            response = requests.post(GROBID_URL, files={"input": pdf_file}, data={"consolidate": "1"})

        # Extraer enlaces si la respuesta es válida
        if response.status_code == 200:
            links = extract_reference_links(response.text)# Llama a la función para extraer enlaces

            # Si se encontraron enlaces, los muestra en la consola
            if links:
                print(f"Links encontrados en '{pdf_path}':")
                for link in links:
                    print(f"  - {link}")
            else:
                print(f"No se encontraron links en las referencias de '{pdf_path}'.")
        else:
            print(f"Error procesando '{pdf_path}': Código {response.status_code}")

    except FileNotFoundError:
        print(f"El archivo '{pdf_path}' no se encontró.")
