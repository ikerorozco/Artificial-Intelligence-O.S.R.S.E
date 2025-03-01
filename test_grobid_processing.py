import unittest
import requests
import os
from unittest.mock import patch
import argparse
from io import StringIO
from LinksFound import extract_reference_links
from FigurasPorArticulo import count_figures

class TestGrobidAndExtractFunctions(unittest.TestCase):

    # Test para verificar la conexión con GROBID
    def test_grobid_connection(self):
        """Verificar que la conexión con GROBID se establezca correctamente."""
        grobid_url = "http://localhost:8070/api/processFulltextDocument"  # Cambia esta URL si es necesario

        # Abre un archivo PDF de prueba (asegúrate de tener un archivo PDF de ejemplo en el directorio)
        with open("Boosting Data.pdf", "rb") as f:
            # Envía la solicitud POST con el archivo PDF
            response = requests.post(grobid_url, files={"input": f}, data={"consolidate": "1"})

        # Verificamos que la respuesta sea 200, lo que indica que la conexión fue exitosa
        self.assertEqual(response.status_code, 200, "No se pudo conectar con GROBID.")
        
        # Verificamos que la respuesta contenga un apartado <abstract>
        self.assertIn("<abstract>", response.text, "No se encontró el apartado <abstract> en el PDF procesado.")

    # Test para verificar que el argumento de línea de comandos por defecto es correcto
    @patch('sys.argv', ['script_name'])  # Simula que no se pasan argumentos
    def test_default_argument(self):
        """Verificar que el argumento de línea de comandos por defecto es correcto."""
        parser = argparse.ArgumentParser(description="Extrae el abstract de PDFs usando GROBID y genera una nube de palabras.")
        parser.add_argument("-i", "--input", default="pdfs", help="Carpeta donde están los archivos PDF (por defecto 'pdfs').")
        
        args = parser.parse_args()
        
        # Verificamos que el valor de 'input' sea el valor por defecto
        self.assertEqual(args.input, 'pdfs')

    # Test para verificar si la carpeta 'pdfs' está vacía
    def test_pdfs_directory_is_empty(self):
        """Verificar si la carpeta 'pdfs' está vacía."""
        pdf_directory = 'pdfs'
        if os.path.exists(pdf_directory):
            pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith(".pdf")]
            if len(pdf_files) == 0:
                self.fail("No hay archivos PDF en la carpeta 'pdfs'.")
            else:
                # Si hay archivos PDF, imprimir la lista
                print("Archivos PDF encontrados en la carpeta 'pdfs':")
                for pdf in pdf_files:
                    print(pdf)
        else:
            self.fail("La carpeta 'pdfs' no existe.")

    # Test para contar el número de figuras en el XML procesado
    def test_count_figures(self):
        xml_text = """
    <tei:TEI xmlns:tei="http://www.tei-c.org/ns/1.0">
        <tei:body>
            <tei:figure>Figura 1</tei:figure>
            <tei:figure>Figura 2</tei:figure>
        </tei:body>
    </tei:TEI>
    """
        self.assertEqual(count_figures(xml_text), 2, "La función count_figures no cuenta correctamente las figuras.")

    # Test para verificar que la función extraiga correctamente los enlaces de un XML de prueba
    def test_extract_reference_links(self):
        """Verificar que la función extraiga correctamente los enlaces de un XML de prueba."""
        # Simulamos un XML de prueba con enlaces
        xml_text = """
        <tei:TEI xmlns:tei="http://www.tei-c.org/ns/1.0">
            <tei:pubNote>
                <tei:biblStruct>
                    <tei:ptr target="https://link1.com"/>
                </tei:biblStruct>
                <tei:biblStruct>
                    <tei:ptr target="https://link2.com"/>
                </tei:biblStruct>
            </tei:pubNote>
        </tei:TEI>
        """
        
        # Llamamos a la función y verificamos los enlaces extraídos
        links = extract_reference_links(xml_text)
        self.assertEqual(links, ["https://link1.com", "https://link2.com"], "Los enlaces extraídos no son correctos.")

if __name__ == '__main__':
    unittest.main()
