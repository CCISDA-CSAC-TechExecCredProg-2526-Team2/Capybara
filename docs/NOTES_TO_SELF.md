# 1️⃣ Auto-sync docs/changelog.md from root CHANGELOG.md
Right now, your docs Changelog page is static, which is why you’re seeing the placeholder text.
Replace contents of docs/changelog.md with:

\# Changelog

```{include} ../CHANGELOG.md
:relative-docs: docs/```

## What this does
- Pulls in the **root** `CHANGELOG.md`
- Keeps a **single source of truth**
- Updates automatically on every build
- Preserves markdown formatting
## 📌 This works because:
- You already have `myst_parser`
- RTD allows relative includes **one level up**
---
## ⚠️ Important note
Do **not** delete `docs/changelog.md`.  
Sphinx needs a file inside `docs/` to anchor navigation.
---

---

# 2️⃣ Adding a logo to the top of the navigation menu
This is controlled entirely in `conf.py`.
---
## Step 1: Add your logo file
(Transparent PNG or SVG works best.)
---
## Step 2: Update `conf.py`

Add or update these lines:

```python
html_logo = "_static/capybara-logo.png"
html_theme_options = {
    "logo_only": True,
    "display_version": False,
}```

---

# 3️⃣ Why it says “Original Edition (1.x)” instead of “Alpha Edition (0.0.1)”
Read the Docs versioning UI ≠ your document content.
Right now:
- RTD is showing its default “latest” version
- RTD assumes 1.x until you tell it otherwise
- Your edition metadata is in conf.py, but
- RTD’s sidebar version selector is controlled outside Sphinx
✅ Immediate fix (Sphinx-side, no RTD UI yet)
Make sure your conf.py explicitly defines the current edition:
```edition_name = "Alpha Edition"
edition_codename = "Alpha"
version = "0.0.1"
release = "0.0.1"
edition_full = f"{edition_name} {release}"
project = "Capybara Framework"
html_title = f"{project} - {edition_full}"```

