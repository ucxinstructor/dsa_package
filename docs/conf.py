import os
import sys

# Add the src folder to sys.path so Sphinx can import your package
sys.path.insert(0, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------
project = "ucxdsa"
author = "Carl Limsico"
copyright = "2025, Carl Limsico"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",       # for Google/NumPy docstrings
    "sphinx.ext.autosummary",    # generate pages for each class/function
    "sphinx_autodoc_typehints"
]

autosummary_generate = True     # generate stub files automatically

# Mock imports to prevent hanging if packages are missing
autodoc_mock_imports = ["matplotlib", "networkx"]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
