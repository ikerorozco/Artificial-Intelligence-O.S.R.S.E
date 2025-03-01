# Rationale para Tests en Grobid

1. Conexión con GROBID (`test_grobid_connection`)

1. Se envía una solicitud HTTP POST a la URL de GROBID (especificada en el test).
2. El archivo PDF de prueba, denominado "Boosting Data.pdf", se envía como parte de la solicitud.
3. Se espera que la respuesta de GROBID sea un código de estado 200, lo que indica que la conexión fue exitosa.
4. Se verifica que la respuesta del servidor contenga el apartado `<abstract>`, que indica que el procesamiento del PDF fue realizado correctamente.

Verificación:
- El test pasará si el código de estado de la respuesta es 200.
- El test pasará si el XML procesado contiene la etiqueta `<abstract>`.

2. Argumento de Línea de Comandos por Defecto (`test_default_argument`)

1. Se simula que no se pasan argumentos en la línea de comandos utilizando `@patch` de `unittest.mock`.
2. Se analiza el valor del argumento `input` del parser, que debe ser "pdfs" por defecto.

Verificación:
- El test pasará si el valor del argumento `input` es igual a "pdfs".

3. Comprobación de la Carpeta 'pdfs' Vacía (`test_pdfs_directory_is_empty`)

1. Se verifica si la carpeta "pdfs" existe.
2. Si la carpeta existe, se comprueba si contiene archivos con extensión `.pdf`.
3. Si la carpeta está vacía o no existe, el test fallará.

Verificación:
- El test pasará si la carpeta "pdfs" contiene al menos un archivo PDF.
- El test fallará si no se encuentran archivos PDF o si la carpeta no existe.

4. Contar el Número de Figuras en un XML (`test_count_figures`)

1. Se proporciona un XML de prueba que contiene dos figuras.
2. Se llama a la función `count_figures` para contar las etiquetas `<tei:figure>`.
3. Se compara el resultado con el número esperado (2 figuras).

Verificación:
- El test pasará si la función devuelve 2 como el número de figuras.

5. Extracción de Enlaces de un XML de Prueba (`test_extract_reference_links`)

1. Se proporciona un XML de prueba con enlaces dentro de las etiquetas `<tei:ptr>`.
2. Se llama a la función `extract_reference_links`, que debe extraer los valores de los atributos `target` de las etiquetas `<tei:ptr>`.
3. Se compara el resultado con la lista esperada de enlaces.

Verificación:
- El test pasará si los enlaces extraídos coinciden con los enlaces esperados, en este caso `["https://link1.com", "https://link2.com"]`.

Si todos los tests pasan, se garantiza que las funciones implementadas cumplen con los requisitos del proyecto.
