import sys
import os

sys.path.insert(0, os.path.abspath('../..'))

project = 'sensingpy'
copyright = '2025, Sergio Heredia'
author = 'Sergio Heredia'
release = '2.1.2'
version = '2.1.2'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    "nbsphinx",
    'IPython.sphinxext.ipython_console_highlighting',
]

nbsphinx_allow_errors = True
nbsphinx_execute = 'never'

# Disable autosummary generation to avoid duplicates with automodule
autosummary_generate = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/generated']

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_extra_path = ['.nojekyll']
html_baseurl = 'https://aouei.github.io/sensingpy/'