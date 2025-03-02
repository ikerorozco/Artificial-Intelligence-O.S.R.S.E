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
Créditos
---------
Este proyecto fue desarrollado para facilitar la extracción y análisis de información en documentos científicos.
Si tienes sugerencias o mejoras, ¡no dudes en contribuir!

