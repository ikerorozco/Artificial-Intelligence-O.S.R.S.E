[![DOI](https://zenodo.org/badge/924684829.svg)](https://doi.org/10.5281/zenodo.14911491)

Visita la documentacion oficial en : https://artificial-intelligence-osrse.readthedocs.io
# Grobid use with Python
# Artificial-Intelligence-O.S.R.S.E
Repositorio creado para la ver los cambios realizados en la materia
- Proper documentation (readthedocs + readme)

- Description

Este proyecto está diseñado para enseñar cómo crear repositorios que sigan las mejores prácticas de desarrollo, lo que asegura que el software sea accesible, fácilmente encontrable, interoperable y reusable. A través de este proyecto, aprenderemos cómo estructurar el código de manera adecuada, cómo escribir documentación clara y útil, y cómo seguir los estándares que permiten que el software se utilice de manera eficiente y efectiva en diferentes entornos. Este repositorio no solo está enfocado en el desarrollo técnico, sino también en cómo garantizar que el proyecto sea fácil de mantener y colaborar con otros desarrolladores, promoviendo así la sostenibilidad y el crecimiento a largo plazo.

A lo largo de esta guía, se proporcionarán las especificaciones básicas necesarias para hacer uso de este proyecto, así como recomendaciones clave para asegurar su correcto funcionamiento. Además, se ofrecerán directrices sobre las mejores prácticas que deben seguirse al utilizar este software, asegurándose de que los detalles importantes no se pierdan y que se aproveche al máximo el potencial de la herramienta. Al seguir esta guía, se pretende que los usuarios puedan ejecutar, modificar y extender el software sin dificultad, mejorando la comprensión y aprovechamiento del proyecto.

Este software utiliza un servidor Grobid en conjunto con un entorno de ejecución localhost para extraer y procesar información relevante de documentos en formato PDF. Grobid, que es una herramienta avanzada para la extracción de metadatos y estructuras de documentos académicos, permite analizar artículos científicos y obtener datos valiosos como el número de figuras, las citas, las referencias, y mucho más. A través de este proyecto, implementamos diversas técnicas avanzadas de análisis de texto. Estas funcionalidades facilitan un análisis profundo y exhaustivo de los documentos, ayudando a transformar datos no estructurados en información útil y visualmente accesible.

- Requirements

  Grobid (versión recomendada: 0.8.1)
  
  Python (versión recomendada: >=3.8)
  
  Docker (última versión estable)
  
  Anaconda (última versión estable)
  


Ademas de esto se necesitara instalar librerias extras para el uso correcto de este software

Dependencias utilizadas:

fpdf

matplotlib

requests

wordcloud

argparse


Todas estas se encuentran en requirements.txt


- Installation instructions
  

Para empezar se necesitara Descarga e instala Docker desde su página oficial:


🔗 [Docker Official Website](https://www.docker.com)


a partir de aqui se descargara la version, esto depende de tu sistema operativo y se debera de seguir la descarga como se es habitual


Verifica que Docker está instalado correctamente ejecutando:


docker --version

Asegurese de que Docker este en ejecucion para la siguiente parte


Despues podremos empezar con la descarga de grobid para esto vamos a usar la ultima Stable release


Grobid requiere Java 11 o superior. Puedes verificar si lo tienes con:


-java -version

si se tiene java 11 se deberia de mostrar un mensaje parecido a este

openjdk version "11.0.XX"

OpenJDK Runtime Environment

OpenJDK 64-Bit Server VM



si no se cuenta se puede instalar desde la linea de comandos con

winget search openjdk
winget install --id Microsoft.OpenJDK.11


o si se prefiere con oracle se escribe en linea de comandos

winget search java
winget install --id Oracle.JDK.11



Escribiremos en consola:


  wget https://github.com/kermitt2/grobid/archive/0.8.1.zip
  

Despues de esto se necesitara ejecutar un 


  unzip 0.8.1.zip
  

Ya que tengamos grobid descomprimido podremos usarlo un server desde Docker escribiendo en la linea de comandos


  docker run --rm --gpus all --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.1
  

Dale algo de tiempo para que pueda iniciar el servidor con facilidad, podras confrimar que funciona visitando


  http://localhost:8070
  

y debe de aparecer grobid preparado y listo para usar


Despues de esto se debera de descargar la ultima version estable de Conda, la cual permitira descargar sin ningun problema el environment que se necesite, puede encontrar la pagina oficial para descargar en:


https://www.anaconda.com/download


Despues de esto se debera de clonar este repositorio desde una carpeta a su eleccion, se hara en la linea de comandos y agregando el siguiente comando:


git clone https://github.com/ikerorozco/Artificial-Intelligence-O.S.R.S.E.git

se debera de entrar a la carpeta de github recien copiada


cd Artificial-Intelligence-O.S.R.S.E


y crear el environment deseado


conda env create -f environment.yml


conda activate "Ejemplo" se puede cambiar el nombre a gusto personal

Si los comandos de conda no se pueden ejecutar, es importante que se cambie a la consola especifica que viene con la instalacion de conda, entrar desde consola a la localizacion de la carpeta donde se clono el repositorio y ejecutar estos comandos de conda


Ya se tienen todos los requisitos necesarios para usar el codigo, ahora solo se necesita localizar en donde se clono su repositorio, dentro de la carpeta Artificial-Intelligence-O.S.R.S.E se debe de crear una carpeta llamada data y dejar ahi los PDFs, si no se quiere llamar asi la carpeta se puede nombrar de otra manera pero se debera de especificar el nombre como se vera en el apartado "Execution instructions"



- Execution instructions
  

Para ejecutar se deberan de cumplir con los siguientes requerimientos:


  -Tener Descargados los programas que se quieran ejecutar
  
  -Tener Docker corriendo con Grobid en http://localhost:8070. 
  
  -Para usarlos se debera de tener en la misma carpeta donde se descargaron los pdf que se quieran procesar
  
  -Los pdf son recomendables que esten en ingles y en el caso de el programa "KeyWordCloud.py" contar con un apartado de abstract, de lo contrario funcionara de forma correcta
  
  -Dependiendo del programa si no se quiere tener una carpeta llamada data, se puede tambien ejecutar de la siguiente maneta
  

    python KeyWordCloud.py -i "Nombre de la carpeta" para que el programa funcione de manera optima
    python FigurasPorArticulo.py -i "Nombre de la carpeta" para que el programa funcione de manera optima
    python LinksFound.py -i "Nombre de la carpeta" para que el programa funcione de manera optima -o "Nombre de pdf de salida" si no se especifica se dara un predeterminado


Estos programas se pueden ejecutar tanto en consola como en visual studio, con su contenedor en Dcoker (Pasos de instalacion con Docker mas adelante) o en su editor de codigo con consola de preferencia siempre y cuando haya seguido los pasos de instalacion

  
- Running example(s)

  se debera de ingresar desde el lugar donde se clono el repositorio a la consola 

  -Para el primer programa se debera de escribir en consola python KeyWordCloud.py -i "Nombre de la carpeta"
  
    -si la ejecucion fue exitosa se debera de mostrar en consola este mensaje "Abstract extraído:" y las primeras palabras del abstract encontrado ademas de una ventana emergente con el KeyWordCloud
  
    -si la ejecucion NO fue exitosa se mostrara este mensaje "No se encontró un abstract en el documento." el cual nos muestra que el pdf no cuenta con el apartado abstract
  
    -si la ejecucion NO fue exitosa se mostrara este mensaje "Error en la solicitud a GROBID:" el cual nos muestra que probablemente el problema sea la ejecucion de grobid en localhost 8070 (se recomienda verificar si funciona en su computadora con un pdf de prueba)
  
  
  -Para el segundo programa se debera de escribir en consola python FigurasPorArticulo.py -i "Nombre de la carpeta"
  
    -si la ejecucion fue exitosa se debera de mostrar en consola este mensaje "Ejemplo.pdf : 5 figuras encontradas:" mientras mas PDFs en la carpeta mas respuestas se mostraran en consola Ademas de una grafica de barras que nos dira cuantas figuras encontro por pdf
  
    -si la ejecucion NO fue exitosa se mostrara este mensaje "Error procesando Ejemplo.pdf: Código (codigo asociado al problema en GROBID)." el cual nos muestra que probablemente el problema sea la ejecucion de grobid en localhost 8070 (se recomienda verificar si funciona en su computadora con un pdf de prueba)
  

  -Para el tercer programa se debera de escribir en consola python LinksFound.py -i "Nombre de la carpeta" -o "Nombre de pdf de salida"
  
    -si la ejecucion fue exitosa se debera de mostrar en consola este mensaje "Links encontrados en Ejemplo.pdf" y seguido un valor numerico, mientras mas pdfs mas respuestas se mostraran en consola o si el pdf no tiene pdf se mostrara el mensaje "No se encontraron links en las referencias de Ejemplo.pdf"
  
    -si la ejecucion NO fue exitosa se mostrara este mensaje "Error procesando Ejemplo.pdf: Código (codigo asociado al problema en GROBID)." el cual nos muestra que probablemente el problema sea la ejecucion de grobid en localhost 8070 (se recomienda verificar si funciona en su computadora con un pdf de prueba)

- Descarga alternativa con Docker

  Con esta descarga se contempla algun fallo relacionado con el sistema operativo o errores fuera de el alcance del software, por ende se desarrollara una guia para que se pueda reproducir mediante Dockers y contenedores adicionales, lo primero que se necesitara hacer es apagar todos los contenedores, ya que las instrucciones de Docker lo haran por ti

  docker container prune -f "cuidado al ejecutar ya que si se tienen contenedores de proyectos personales tambien pararan"

ya que se tengan todos los requerimientos previamente dichos, se debera de ingresar desde el lugar donde se clono el repositorio a la consola y colocar este comando

  docker-compose build

  docker-compose up

Si todo salio bien al ejecutar este comando se podran ver los contenedores que se estan ejecutando

docker ps

por ultimo pueden surgir problemas si no se tiene la carpeta de "data" en la carpeta donde se clono el repositorio y dara problemas con el volumen establecido, por ende es imoprtante agregar esta carpeta

- Preferred citation
  

cff-version: 1.2.0

message: "If you use this software, please cite it as below."

authors:

  - family-names: Orozco_Hernandez
  - 
    given-names: Iker
    
    orcid: https://orcid.org/0009-0005-6369-1755
    
title: "Grobid use on Python"

version: 2.0.0

identifiers:

  - type: doi
  - 
    value: DOI: 10.5281/zenodo.14911493
    
date-released: 2025-03-02



- Where to get help
- 

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
