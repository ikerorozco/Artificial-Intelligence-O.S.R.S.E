.. Proyecto de Extracción de Datos con GROBID
==================================================

Bienvenido a la documentación del **Proyecto de Extracción de Datos con GROBID**.
Este conjunto de herramientas permite extraer información relevante desde archivos PDF, como **resúmenes (abstracts)** y **enlaces de referencias**, utilizando la API de GROBID.

.. contents:: Tabla de Contenidos
   :depth: 2
   :local:
   :backlinks: top

Introducción
-------------
Esta documentación cubre el uso de los scripts disponibles en este proyecto para procesar documentos científicos y generar representaciones visuales de datos clave.

Instalación
------------
Para ejecutar estos scripts, necesitas instalar los siguientes paquetes en tu entorno:

.. code-block:: bash

   "pip install requests wordcloud matplotlib fpdf"

Además, asegúrate de tener un servidor GROBID en funcionamiento en `http://localhost:8070`.

Uso de los Scripts
-------------------
El proyecto cuenta con las siguientes herramientas:

 **Generador de Nube de Palabras** (`KeyWordCloud.rst`)
   - Extrae el abstract de PDFs.
   - Genera una nube de palabras basada en palabras clave.

 **Extractor de Enlaces** (`linksFound.rst`)
   - Extrae enlaces de referencias en los PDFs.
   - Genera un archivo PDF con la lista de enlaces encontrados.

 **Extractor de Figuras** (`FigurasPorArticulo.rst`)
   - Busca todas las imagenes de los PDFs.
   - Genera una grafica de barras con la cantidad de imagenes por PDF.

Ejemplo de Uso
--------------
Ejecuta los scripts con la siguiente estructura:

Para generar una nube de palabras:

.. code-block:: bash

  "python keyword_cloud.py -i pdfs/"

Para extraer enlaces de referencias:

.. code-block:: bash

   "python links_extractor.py -i pdfs/ -o Enlaces_Extraidos.pdf
"
FigurasPorArticulo module
=========================

FigurasPorArticulo
==================

Este módulo permite analizar archivos PDF y extraer la cantidad de figuras contenidas en ellos utilizando el servicio GROBID. Genera una gráfica de barras con el número de figuras detectadas en cada documento.


Descripción General
-------------------
El script procesa una carpeta con archivos PDF, los envía al servicio GROBID para su análisis y extrae la cantidad de figuras presentes en cada documento. Finalmente, genera una gráfica de barras mostrando los resultados.


Uso del Script
--------------
El script puede ejecutarse desde la línea de comandos con la siguiente sintaxis:

.. code-block:: bash

   python FigurasPorArticulo.py -i <ruta_de_la_carpeta_con_pdfs>

Si no se especifica una ruta, se tomará la carpeta `pdfs` como directorio por defecto.

-Para este programa se debera de escribir en consola python FigurasPorArticulo.py -i "Nombre de la carpeta"

-si la ejecucion fue exitosa se debera de mostrar en consola este mensaje "Ejemplo.pdf : 5 figuras encontradas:" mientras mas PDFs en la carpeta mas respuestas se mostraran en consola Ademas de una grafica de barras que nos dira cuantas figuras encontro por pdf

-si la ejecucion NO fue exitosa se mostrara este mensaje "Error procesando Ejemplo.pdf: Código (codigo asociado al problema en GROBID)." el cual nos muestra que probablemente el problema sea la ejecucion de grobid en localhost 8070 (se recomienda verificar si funciona en su computadora con un pdf de prueba)

Dependencias
------------
Para ejecutar este script, se requieren las siguientes librerías:

fpdf

matplotlib

requests

wordcloud

argparse


Funciones Principales
---------------------

1. **count_figures(xml_text)**

   Extrae el número de figuras presentes en el XML devuelto por GROBID.

   **Parámetros:**
   - `xml_text` (str): Contenido del XML procesado por GROBID.

   **Retorno:**
   - (int): Número de figuras encontradas en el documento.


2. **Procesamiento de PDFs**

   - Se verifica que la carpeta especificada exista.
   - Se obtiene la lista de archivos PDF en la carpeta.
   - Cada PDF se envía a GROBID para su análisis.
   - Se extrae el número de figuras por documento y se almacena en un diccionario.
   - Si no se encuentran figuras, el programa finaliza con un mensaje de aviso.


3. **Generación de Gráfica**

   - Se construye una gráfica de barras con `matplotlib` mostrando la cantidad de figuras detectadas por documento.
   - Se ajustan etiquetas y formatos para una mejor visualización.
   - Se muestra la gráfica al usuario.


Ejemplo de Código
-----------------

.. code-block:: python

   from FigurasPorArticulo import count_figures

   xml_data = """<TEI xmlns='http://www.tei-c.org/ns/1.0'>
   <figure><figDesc>Diagrama 1</figDesc></figure>
   <figure><figDesc>Diagrama 2</figDesc></figure>
   </TEI>"""

   print(count_figures(xml_data))  # Salida esperada: 2


Mensajes de Error
-----------------

El script maneja varias excepciones y errores posibles:

- Si la carpeta de PDFs no existe, el programa termina con un mensaje de error.
- Si la carpeta está vacía, se muestra un mensaje y el programa finaliza.
- Si el servicio de GROBID no responde o devuelve un código de error, se muestra el código de estado correspondiente.
- Si no se encuentran figuras en ningún documento, el script finaliza sin generar la gráfica.


Consideraciones
---------------

- Es necesario que GROBID esté corriendo en `http://localhost:8070` para que el script funcione correctamente.
- Se recomienda instalar las dependencias en un entorno virtual para evitar conflictos de paquetes.


Conclusión
----------

Este módulo es útil para analizar rápidamente archivos PDF en busca de figuras y obtener una representación visual de la cantidad de imágenes en cada documento. Puede adaptarse para realizar análisis más detallados o integrarse en otros sistemas de procesamiento de textos científicos.



Créditos
---------
Este proyecto fue desarrollado para facilitar la extracción y análisis de información en documentos científicos.
Si tienes sugerencias o mejoras, ¡no dudes en contribuir!

