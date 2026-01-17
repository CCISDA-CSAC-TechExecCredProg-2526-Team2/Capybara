version: 2

# Configuration file for the Sphinx documentation builder.

# Capybara is a documentation-only repository. Sphinx is used purely as a documentation compiler for Read the Docs.

# -- Project information -----------------------------------------------------

project = "Capybara"
author = "Capybara Project Authors"
copyright = "2026, Capybara Project Authors"

# -- Capybara Edition Metadata -----------------------------------------------

# Update these values for each release
edition_name = "Alpha Edition"
edition_version = "0.0.1"
edition_full = f"{edition_name} {edition_version}"

# Sphinx-standard version fields
version = edition_version
release = edition_full

# -- General configuration ---------------------------------------------------

extensions = ["myst_parser",]

templates_path = ["_templates"]
exclude_patterns = []

# -- MyST (Markdown) configuration ------------------------------------------

myst_enable_extensions = ["colon_fence", "deflist", "tasklist",]

# -- HTML output -------------------------------------------------------------

html_theme = "sphinx_rtd_theme"

# Static files (CSS, images, etc.)
html_static_path = ["_static"]

# Custom CSS files (Capybara branding)
html_css_files = ["capybara.css",]

# Title shown in browser, sidebar, and search results
html_title = f"Capybara Framework – {edition_full}"

# Clean URLs (recommended for Read the Docs)
html_use_directory_html = True
