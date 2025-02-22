# Artificial-Intelligence-O.S.R.S.E
Repositorio creado para la ver los cambios realizados en la materia
#incluye ejemplos
#usa github copilot
#crear un citation.cff
#crear codemeta generator  JSON-LD file
- Zenodo integration (with a badge in the readme)
- Proper metadata (codemeta, license, releases, citation, etc.)
- Have reproducible instructions on how to set up an environment
- Do not upload the environment to GitHub
- Proper documentation (readthedocs + readme)
- Remember to include both installation methods (env + docker)
- Tests
- Dockerfile + docker run instructions (this is an alternative installation
method to your environment setup). Docker compose is optional

- Description

Este Proyecto nos enseña a crear repositorios con las mejores practicas para poder hacer de este software accesible, encontrable, interoperable y reusable
se daran las especificaciones basicas para su uso, recomendaciones y formas de buen uso mediante esta guia para que no se pierdan de los detalles de hacer
y usar este proyecto

- Requirements

Software que se necesita

  Grobid : (Ultima version)
  Python : (Ultima version)
  Docker : (Ultima version)

Ademas de esto se necesitara instalar librerias extras para el uso correcto de este software

Dependencias utilizadas:

Request
  Descargada desde consola con: pip install requests

WordCloud
  Descargada desde consola con: pip install wordcloud
  
Si se realizara un pip freeze se tendria que ver de la siguiente manera

certifi==2025.1.31
charset-normalizer==3.4.1
contourpy==1.3.1
cycler==0.12.1
fonttools==4.56.0
idna==3.10
kiwisolver==1.4.8
matplotlib==3.10.0
numpy==2.2.3
packaging==24.2
pillow==11.1.0
pyparsing==3.2.1
python-dateutil==2.9.0.post0
requests==2.32.3
six==1.17.0
urllib3==2.3.0
wordcloud==1.9.4

- Installation instructions

Para empezar se necesitara descargar Docker, la version que se esta usando aqui es docker para esto puedes visitar la pagina

  https://www.docker.com

a partir de aqui descargaras la version que depende de tu sistema operativo y sigues la descarga como es habitual

Despues podremos empezar con la descarga de grobid para esto vamos a usar la ultima Stable release

Escribiremos en consola:

  wget https://github.com/kermitt2/grobid/archive/0.8.1.zip
  unzip 0.8.1.zip

Ya que tengamos grobid descomprimido podremos usarlo un server desde Docker con el comando

  docker run --rm --gpus all --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.1

Dale algo de tiempo para que pueda iniciar el servidor con facilidad, podras confrimar que funciona visitando

  http://localhost:8070

y debe de aparecer grobid preparado y listo para usar

- Execution instructions

Para ejecutar se deberan de cumplir con los siguientes requerimientos:

  -Tener Descargados los programas que se quieran ejecutar
  -Para usarlos se debera de tener en la misma carpeta donde se descargaron los pdf que se quieran procesar
  -Los pdf son recomendables que esten en ingles y en el caso de el programa "KeyWordCloud.py" contar con un apartado de abstract, de lo contrario no lo         generara
  -Editar en la parte donde dice "pdf_files" o "pdf_path" el o los nombres de los pdfs que se quieran usar en el programa, simepre con terminacion .pdf

Estos programas se pueden ejecutar tanto en consola como en visual studio o en su editor de codigo con consola de preferencia siempre y cuando haya seguido los pasos de instalacion
  
- Running example(s)

  -Para el primer programa se modificara especificamente "pdf_path = "Ejemplo.pdf"" con el pdf de su preferencia
    -si la ejecucion fue exitosa se debera de mostrar en consola este mensaje "Abstract extraído:" y las primeras palabras del abstract encontrado
      ademas de una ventana emergente con el KeyWordCloud 
    -si la ejecucion NO fue exitosa se mostrara este mensaje "No se encontró un abstract en el documento." el cual nos muestra que el pdf no cuenta con el         apartado abstract
    -si la ejecucion NO fue exitosa se mostrara este mensaje "Error en la solicitud a GROBID:" el cual nos muestra que probablemente el problema sea la          ejecucion de grobid en localhost 8070 (se recomienda verificar si funciona en su computadora con un pdf de prueba)
  
  -Para el segundo programa se modificara especificamente "pdf_files = ["Ejemplo.pdf"]" con los pdf de su preferencia
    -si la ejecucion fue exitosa se debera de mostrar en consola este mensaje "Ejemplo.pdf : 5 figuras encontradas:" mientras mas pdfs mas respuestas se           mostraran en consola Ademas de una grafica de barras que nos dira cuantas figuras encontro por pdf
    -si la ejecucion NO fue exitosa se mostrara este mensaje ""Error procesando Ejemplo.pdf: Código (codigo asociado al problema en GROBID)." el cual nos         muestra que probablemente el problema sea la ejecucion de grobid en localhost 8070 (se recomienda verificar si funciona en su computadora con un pdf de      prueba)

  -Para el tercer programa se modificara especificamente "pdf_files = ["Ejemplo.pdf"]" con los pdf de su preferencia
    -si la ejecucion fue exitosa se debera de mostrar en consola este mensaje "Links encontrados en Ejemplo.pdf" y seguido de varios links mientras mas pdfs mas respuestas se mostraran en consola o si el pdf no tiene pdf se mostrara el mensaje "No se encontraron links en las referencias de Ejemplo.pdf"
    -si la ejecucion NO fue exitosa se mostrara este mensaje ""Error procesando Ejemplo.pdf: Código (codigo asociado al problema en GROBID)." el cual nos muestra que probablemente el problema sea la ejecucion de grobid en localhost 8070 (se recomienda verificar si funciona en su computadora con un pdf de      prueba)
    -si la ejecucion NO fue exitosa se mostrara este mensaje "El archivo Ejemplo.pdf no se encontró." el cual quiere decir que el programa no encuentra el archivo con el mismo nombre escrito en el codigo, lo mejor seria revisar que sea el mismo nombre o la terminacion del archivo

- Preferred citation (who is the main author?)


- Where to get help

Si tiene dudas de como usar GROBID, instalacion o llamado a local host 8070, puede visitar su documentacion oficial
  https://grobid.readthedocs.io/en/latest/

Si tiene alguna duda con el funcionamiento de el codigo python puede escribir su consulta a mi correo electronico
  Ikerorozcoh@gmail.com

  
@misc{GROBID,
    title = {GROBID},
    howpublished = {\url{https://github.com/kermitt2/grobid}},
    publisher = {GitHub},
    year = {2008--2025},
    archivePrefix = {swh},
    eprint = {1:dir:dab86b296e3c3216e2241968f0d63b68e8209d3c}
}
