'''import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx_odev'
copyright = '2025, Rüya Beste'
author = 'Rüya Beste'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

extensions = [
    'sphinx.ext.autodoc',
]

html_theme = 'sphinx_rtd_theme' '''


import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'sphinx_odev'
copyright = '2025, Rüya Beste'
author = 'Rüya Beste'
release = '0.1'

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

language = 'en'  

html_theme = 'sphinx_rtd_theme' 
html_static_path = ['_static']
