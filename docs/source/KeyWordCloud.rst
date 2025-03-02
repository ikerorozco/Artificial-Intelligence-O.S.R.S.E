KeyWordCloud module
===================

KeyWordCloud
============

Descripción General
-------------------

Este módulo permite extraer el abstract de archivos PDF utilizando GROBID y generar una nube de palabras clave a partir del texto obtenido. La nube de palabras se genera mediante la biblioteca `wordcloud`, representando gráficamente la frecuencia de las palabras más relevantes en el texto procesado.


Uso del Script
--------------

Este módulo se ejecuta a través de la línea de comandos y permite especificar la carpeta donde se encuentran los archivos PDF mediante el argumento `-i` o `--input`.

Ejemplo de ejecución:

```
python KeyWordCloud.py -i pdfs
```

Si no se proporciona el argumento `-i`, por defecto se buscarán archivos en la carpeta `pdfs`.

Dependencias
------------

Para ejecutar este módulo, se requieren las siguientes bibliotecas:

- `requests`
- `xml.etree.ElementTree`
- `wordcloud`
- `matplotlib`
- `collections.Counter`
- `re`
- `argparse`

Funciones Principales
---------------------

1. `extract_abstract(xml_text)`

   - Extrae el texto del abstract desde el XML generado por GROBID.
   - Retorna el texto del abstract si se encuentra, de lo contrario, devuelve `None`.

2. `process_text(text)`

   - Convierte el texto en minúsculas y elimina signos de puntuación y números.
   - Filtra palabras irrelevantes usando una lista ampliada de stopwords.
   - Devuelve un `Counter` con la frecuencia de palabras clave.

Flujo de ejecución
------------------

1. Se carga la lista de archivos PDF en la carpeta de entrada.
2. Cada PDF se envía a GROBID para extraer su estructura en XML.
3. Se obtiene el abstract del documento.
4. Se procesa el texto para eliminar stopwords y obtener palabras clave.
5. Se genera una nube de palabras y se muestra mediante `matplotlib`.

Ejemplo de salida
-----------------

Al ejecutar el código con un conjunto de PDFs, la salida en consola incluirá información como:

```
Procesando: articulo1.pdf
Abstract extraído de articulo1.pdf: "Este estudio analiza la influencia de..."
Se genera una nube de palabras para articulo1.pdf.
```

Además, se mostrará una gráfica con la nube de palabras generada.

Consideraciones
---------------

- Asegúrate de que el servicio de GROBID esté en ejecución en `http://localhost:8070/`.
- Verifica que la carpeta de entrada contiene archivos PDF válidos.
- Se recomienda ejecutar el script en un entorno con soporte gráfico para visualizar la nube de palabras.

Autor
-----

Desarrollado por Iker Orozco Hernández.

