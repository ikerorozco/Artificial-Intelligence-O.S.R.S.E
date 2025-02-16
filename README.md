# Artificial-Intelligence-O.S.R.S.E
Repositorio creado para la ver los cambios realizados en la materia
#NOT hard code pdf
#Mas comentarios en el programa
#incluye ejemplos
#usa github copilot
#hacer un release para mi DOI
#crear un citation.cff
#crear codemeta generator  JSON-LD file

que necesita read me



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
- Running example(s)
- Preferred citation (who is the main author?)
- Where to get help
- Acknowledgements (if any)

  
@misc{GROBID,
    title = {GROBID},
    howpublished = {\url{https://github.com/kermitt2/grobid}},
    publisher = {GitHub},
    year = {2008--2025},
    archivePrefix = {swh},
    eprint = {1:dir:dab86b296e3c3216e2241968f0d63b68e8209d3c}
}
