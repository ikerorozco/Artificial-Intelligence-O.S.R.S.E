# conf.py para Sphinx
# -- Project information -----------------------------------------------------

project = 'Tu Proyecto'
author = 'Tu Nombre'
release = '0.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Para generar documentación de código Python
    'sphinx.ext.viewcode', # Para mostrar código fuente
]

templates_path = ['_templates']
exclude_patterns = []

# -- Master document --------------------------------------------------------
# Este es el archivo principal que Sphinx debe usar para generar la documentación
master_doc = 'index'

html_theme = 'default'
