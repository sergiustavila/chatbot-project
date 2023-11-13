""" Configuration file for the Sphinx documentation builder. """
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

from typing import List

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "recommonmark",
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]
exclude_patterns: List[str] = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#pylint: disable=C0103
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


def setup(app):
    """Setup css"""
    app.add_css_file("my_theme.css")
