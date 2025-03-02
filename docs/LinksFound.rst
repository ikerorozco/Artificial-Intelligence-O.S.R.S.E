LinksFound module
=================

LinksFound
==========

Descripción General
-------------------
Este script extrae los enlaces de las referencias bibliográficas en documentos PDF utilizando GROBID y genera un archivo PDF con la lista de enlaces extraídos.

Requisitos
--------------
- Python 3.x
- GROBID en ejecución (por defecto en `http://localhost:8070`)
- Librerías necesarias:
  - `requests`
  - `xml.etree.ElementTree`
  - `fpdf`
  - `argparse`

Puedes instalarlas con:
```sh
pip install requests fpdf
```

Uso del Script
--------------

Ejecuta el script desde la línea de comandos:
```sh
python linksFound.py -i <carpeta_con_pdfs> -o <nombre_del_pdf_salida>
```
Parámetros:
- `-i`, `--input`: Carpeta donde están los archivos PDF (por defecto `pdfs`).
- `-o`, `--output`: Nombre del archivo PDF de salida con los enlaces extraídos (por defecto `Enlaces_Extraidos.pdf`).

Funcionamiento
--------------
1. Verifica que la carpeta de entrada exista y contenga archivos PDF.
2. Procesa cada PDF enviándolo a GROBID para extraer sus referencias.
3. Extrae los enlaces de las referencias bibliográficas en el XML de GROBID.
4. Guarda los enlaces en un archivo PDF con el formato:
   - Nombre del documento
   - Lista de enlaces extraídos
   - Indicación si no se encontraron enlaces

Ejemplo de salida en PDF
------------------------
```
Lista de Enlaces Extraídos
--------------------------
Documento_1.pdf
https://doi.org/10.1000/xyz123
https://arxiv.org/abs/xyz123

Documento_2.pdf
No se encontraron enlaces.
```

Notas
-----
- Si un PDF no contiene enlaces en sus referencias, el archivo de salida indicará "No se encontraron enlaces".
- Si GROBID no está en ejecución, el script no podrá procesar los PDFs.
- La salida se almacena en la misma carpeta de los PDFs, a menos que se especifique otro destino.

Errores comunes
---------------
- **Error 404 o 500 en GROBID**: Verifica que GROBID esté en ejecución y accesible en `http://localhost:8070`.
- **La carpeta especificada no existe**: Asegúrate de que el directorio de entrada sea correcto.
- **No se encontraron archivos PDF**: Verifica que la carpeta contenga documentos PDF.

Autor
-----
Desarrollado por Iker Orozco Hernández.

