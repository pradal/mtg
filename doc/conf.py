# {# pkglts, sphinx
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Package mtg documentation build configuration file, created by
# sphinx-quickstart on Tue Jul  9 22:26:36 2013.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

import pydata_sphinx_theme # Pydata theme: https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# Get the project root dir, which is the parent dir of this
cwd = os.getcwd()
project_root = os.path.dirname(cwd)

# Insert the project root dir as the first element in the PYTHONPATH.
# This lets us ensure that the source package is imported, and that its
# version is used.
sys.path.insert(0, os.path.join(project_root, 'src'))

# import mtg as mypkg

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_favicon',      # support for favicon
    'nbsphinx',     # for integrating jupyter notebooks
    'myst_parser'   # for parsing .md files
]

# try to add more extensions which are not default
# but still useful
# based on the fact that the extension is installed on the system

try:
    import matplotlib.sphinxext.plot_directive
    extensions.append('matplotlib.sphinxext.plot_directive')
except ImportError:
    pass

# default settings that can be redefined outside of the pkglts block
todo_include_todos = True
autosummary_generate = True
intersphinx_mapping = {'python': ('https://docs.python.org/', None)}
inheritance_node_attrs = dict(shape='ellipse', fontsize=12,
                              color='orange', style='filled')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'openalea.mtg'
copyright = u'2015-2025, openalea.mtg'

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#

# find version number in /src/$pkg_pth/version.py
pkgver = {}
with open("../src/openalea/mtg/version.py") as fp:
    exec(fp.read(), pkgver)

# The short X.Y version.
version = pkgver["__version__"]
# The full version, including alpha/beta/rc tags.
release = pkgver["__version__"]


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to
# some non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build', 'dist']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built
# documents.
# keep_warnings = False


# -- Options for HTML output -------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pydata_sphinx_theme'
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
  "header_links_before_dropdown": 6,
  "sidebarwidth": 200,
  "sticky_navigation": "false",
  "collapse_navigation": "false",
  "display_version": "true",
  "icon_links": [
    {
        "name": "GitHub",
        "url": "https://github.com/openalea/openalea.rtfd.io",
        "icon": "fa-brands fa-github",
    },
    ],
    "show_version_warning_banner": True,
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "secondary_sidebar_items": {
        "**/*": ["page-toc", "edit-this-page", "sourcelink"],
        "examples/no-sidebar": [],
    },
  }
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = "_static/openalea_web.svg"
html_favicon = "_static/openalea_web.svg"
# If false, no module index is generated.
html_domain_indices = True
# If false, no index is generated.
html_use_index = True
# If true, the index is split into individual pages for each letter.
html_split_index = False
# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True
# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True
# Output file base name for HTML help builder.
htmlhelp_basename = 'mtg_documentation'

# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    ('index', 'mtg.tex',
     u'mtg Documentation',
     u'Christophe Pradal', 'manual'),
]

# The name of an image file (relative to this directory) to place at
# the top of the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings
# are parts, not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'mtg',
     u'mtg Documentation',
     [u'Christophe Pradal'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'mtg',
     u'mtg Documentation',
     u'Christophe Pradal',
     'mtg',
     'Multiscale Tree Graph datastructure and interfaces',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# use apidoc to generate developer doc
import os
from os import path

from sphinx.ext.apidoc import main

rootpath = path.abspath(path.join(project_root, "src"))
destdir = path.abspath(path.join(project_root, "doc", "_dvlpt"))

if not path.isdir(destdir):
    os.makedirs(destdir)

main(['-e', '-o', destdir, '-d', '4', '-s', source_suffix[1:], '--force', rootpath])

# #}
