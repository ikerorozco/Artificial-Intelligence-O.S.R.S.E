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

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
