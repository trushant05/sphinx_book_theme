import os

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx Book Theme Template'
copyright = '2025, Trushant Adeshara'
author = 'Trushant Adeshara'

# Read verson from the package
with open(os.path.join(os.path.dirname(__file__), "..", "VERSION")) as f:
    full_version = f.read().strip()
    version = ".".join(full_version.split(".")[:3])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming ith Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

# Supported file extensions for source files
source_suffix = {
    '.rst': "restructuredtext",
    '.md': "markdown",
}

# Add any paths that contain templates here, realative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match file and 
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_paths.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "README.md"]

# -- Internationalization ----------------------------------------------------

# specifying the natural language populates some key tags
language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_book_theme

html_title = "Sphinx Book Theme Template"
html_theme_path = [sphinx_book_theme.get_html_theme_path()]
html_theme = "sphinx_book_theme"
#TODO Add logo of the project
#html_favicon = "source/_static/favicon.ico"
html_show_copyright = True
html_show_sphinx = False
html_last_updated_fmt = "" # To reveal the build data in the pages meta

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are coped after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["source/_static/css"]
html_css_files = ["custom.css"]

html_theme_options = {
    "path_to_docs": "docs/",
    "collapse_navigation": True,
    "repository_url": "https://github.com/trushant05/sphinx_book_theme_template",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "show_toc_level": 1,
    "use_sidenotes": True,
}