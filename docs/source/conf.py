import os
import sys

# Asegurar que Sphinx encuentra tu código fuente
sys.path.insert(0, r"C:\Users\ikero\Desktop\PDFs IA\Proyecto Individual")


# -- Project information -----------------------------------------------------
project = 'Artificial-Intelligence-O.S.R.S.E'
copyright = '2025, Iker Orozco'
author = 'Iker Orozco'
release = '1.4'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'default'


# -- Autodoc settings --------------------------------------------------------
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True
}

numfig = True  # Números en secciones
nitpicky = False  # No detenerse por errores menores
