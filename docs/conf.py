version: 2


# ============================================================
# Capybara Sphinx Configuration
# ============================================================

from pathlib import Path


# ------------------------------------------------------------
# Paths
# ------------------------------------------------------------

DOCS_DIR = Path(__file__).parent
ROOT_DIR = DOCS_DIR.parent
EDITIONS_DIR = DOCS_DIR / "editions"


# ------------------------------------------------------------
# Project information (immutable)
# ------------------------------------------------------------

project = "Capybara"

author_original = "Capybara Project Authors"
authors_supplemental = ""  # Subsequent contributors separated by '; '

author_parts = [author_original]
if authors_supplemental:
    author_parts.append(authors_supplemental)

author = "; ".join(author_parts)

copyright_original = "© 2026 Capybara Project Authors"
copyright_supplemental = ""  # Subsequent copyright infos separated by '; '

copyright_parts = [copyright_original]
if copyright_supplemental:
    copyright_parts.append(copyright_supplemental)

copyright = "; ".join(copyright_parts)


# ------------------------------------------------------------
# Capybara Edition Metadata (defaults)
# ------------------------------------------------------------

edition_name = "Alpha Edition"
edition_version = "0.0.1"
edition_tagline = "The Under-Construction Pre-Beta Development Edition"
edition_description = "Alpha edition of the Capybara Framework."
edition_full = f"{edition_name} {edition_version}"

# Sphinx-standard version fields
version = edition_version
release = edition_full


# ------------------------------------------------------------
# Detect current edition directory
# ------------------------------------------------------------

current_edition_slug = None

if EDITIONS_DIR.exists():
    for edition_path in sorted(EDITIONS_DIR.iterdir()):
        if edition_path.is_dir() and (edition_path / "index.md").exists():
            current_edition_slug = edition_path.name
            break

if current_edition_slug:
    CURRENT_EDITION_DIR = EDITIONS_DIR / current_edition_slug
else:
    CURRENT_EDITION_DIR = None


# ------------------------------------------------------------
# Load edition VERSION overrides (if present)
# ------------------------------------------------------------

if CURRENT_EDITION_DIR:
    version_file = CURRENT_EDITION_DIR / "VERSION"

    if version_file.exists():
        edition_vars = {}

        with version_file.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key, value = line.split("=", 1)
                edition_vars[key.strip()] = value.strip().strip('"')

        edition_name = edition_vars.get("edition_name", edition_name)
        edition_version = edition_vars.get("edition_version", edition_version)
        edition_tagline = edition_vars.get("edition_tagline", edition_tagline)
        edition_description = edition_vars.get(
            "edition_description", edition_description
        )

        authors_supplemental = edition_vars.get(
            "author_supplemental", authors_supplemental
        )
        copyright_supplemental = edition_vars.get(
            "copyright_supplemental", copyright_supplemental
        )

        # Rebuild derived fields
        edition_full = f"{edition_name} {edition_version}"
        version = edition_version
        release = edition_full

        author_parts = [author_original]
        if authors_supplemental:
            author_parts.append(authors_supplemental)
        author = "; ".join(author_parts)

        copyright_parts = [copyright_original]
        if copyright_supplemental:
            copyright_parts.append(copyright_supplemental)
        copyright = "; ".join(copyright_parts)


# ------------------------------------------------------------
# General Sphinx configuration
# ------------------------------------------------------------

# Capybara is a documentation-only repository. Sphinx is used purely as a documentation compiler for Read the Docs.

html_favicon = "_static/favicon.ico"

extensions = ["myst_parser",]

templates_path = ["_templates",]

html_sidebars = {
    "**": [
        "logo-text.html",
        "capybara_edition.html",
        "globaltoc.html",
        "relations.html",
        "searchbox.html",
    ]
}

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

master_doc = "index"

language = "en"

# -- MyST (Markdown) configuration ------------------------------------------

myst_enable_extensions = ["substitutions", "colon_fence", "deflist", "tasklist",]


# ------------------------------------------------------------
# HTML output options
# ------------------------------------------------------------

html_theme = "sphinx_rtd_theme"

html_logo = "_static/capybara-logo.png"

html_theme_options = {
    "logo_only": True,
    "display_version": False,
    "collapse_navigation": False,
    "navigation_depth": 4,
    "titles_only": True,
}

html_context = {
    "project": project,
    "edition_name": edition_name,
    "edition_version": edition_version,
    "edition_tagline": edition_tagline,
    "edition_description": edition_description,
    "edition_full": edition_full,
    "version": edition_version,
    "release": edition_full,
}
myst_substitutions = {
    "project": project,
    "edition_name": edition_name,
    "edition_version": edition_version,
    "edition_tagline": edition_tagline,
    "edition_description": edition_description,
    "edition_full": edition_full,
    "version": edition_version,
    "release": edition_full,
}

# Title shown in browser, sidebar, and search results
html_title = f"{project} – {edition_full}"

# Clean URLs (recommended for Read the Docs)
html_use_directory_html = True

# ------------------------------------------------------------
# Static files and CSS (edition-aware)
# ------------------------------------------------------------

html_static_path = ["_static"]

html_css_files = [
    "capybara.css",  # Base styles
]

if CURRENT_EDITION_DIR:
    edition_css = CURRENT_EDITION_DIR / "capybara.css"
    if edition_css.exists():
        html_css_files.append(f"editions/{current_edition_slug}/capybara.css")

# ------------------------------------------------------------
# Read the Docs friendliness
# ------------------------------------------------------------

html_show_sphinx = False
html_show_copyright = True

