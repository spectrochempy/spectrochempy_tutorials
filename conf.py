# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


#
import sphinx_rtd_theme  # Theme for the website

# -- Project information -----------------------------------------------------

project = "SpectroChemPy Tutorials"
copyright = "2022, A. Travert & C. Fernandez"
author = "A. Travert & C. Fernandez"
version = "0.1"
release = ""

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "sphinx_copybutton",
    "sphinx.ext.mathjax",
    'sphinx_rtd_theme',
]

#
# nbsphinx ---------------------------------------------------------------------

#
# List of arguments to be passed to the kernel that executes the notebooks:
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'jpg', 'png'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]

#
# Execute notebooks before conversion: 'always', 'never', 'auto' (default)
nbsphinx_execute = "always"
nbsphinx_allow_errors = True
nbsphinx_timeout = 180

#
# Use this kernel instead of the one stored in the notebook metadata:
nbsphinx_kernel_name = "python3"


nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}

You can run this notebook in a `live session
<https://mybinder.org/v2/gh/spectrochempy/spectrochempy_tutorials/main?labpath=tutorials%2F{{
docname }}>`_ |Binder| or view it on `Github
<https://github.com/spectrochempy/spectrochempy_tutorials/blob/main/source
/tutorials/{{ docname }}>`_ |GitHub|.

.. |Binder| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/spectrochempy/spectrochempy_tutorials/main?labpath=tutorials%2F{{ docname }}

.. |GitHub| image:: https://badgen.net/badge/icon/github?icon=github&label
   :target: https://github.com/spectrochempy/spectrochempy_tutorials/tree/main/tutorials/{{ docname }}

"""

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_templates", "_static", "build", "**.ipynb_checkpoints",
                    "colab", ".*"]


# -- Options for HTML output -------------------------------------------------

#
html_theme = "sphinx_rtd_theme"

#
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "logo_only": False,
    "display_version": True,
    "collapse_navigation": True,
    "navigation_depth": 3,
}

#
# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

#
html_favicon = "_static/scpy.ico"

#
html_logo = "_static/scpy.png"
# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.

#
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

#
# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

#
# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

#
# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

#
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

#
# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

highlight_language = 'none'


def setup(app):
    app.add_css_file("theme_override.css")  # also can be a full URL
