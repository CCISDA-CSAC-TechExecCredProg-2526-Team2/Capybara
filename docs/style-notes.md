# Style Notes and Guidelines

```
    <style>
    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #77390A; /* Heading font color */
    }

    /* Sepia palette swatches */
    .color-swatch {
        display: inline-block;
        width: 60px;
        height: 30px;
        margin: 0 10px 10px 0;
        border: 1px solid #999;
        vertical-align: middle;
        line-height: 30px;
        text-align: center;
        color: #fff;
        font-size: 0.75rem;
        font-family: monospace;
    }

    .sepia1 { background-color: #9F5A2C; }
    .sepia2 { background-color: #77390A; }
    .sepia3 { background-color: #DAC4B0; color: #000; }
    .sepia4 { background-color: #C4A48A; color: #000; }

    /* Blue accents */
    .accent1 { background-color: #39BBFF; }
    .accent2 { background-color: #277DD1; }
    .accent3 { background-color: #0C61B9; }
    .accent4 { background-color: #00356B; }

    </style>
```

## Introduction

This document outlines the **style notes and guidelines** for the Capybara Framework documentation.

All future editions should respect these choices unless explicitly updated in a new edition's "Style Notes and Guidelines" section.


## Color Palette

**Sepia Base Colors**

```
    <div class="color-swatch sepia1">#9F5A2C</div>
    <div class="color-swatch sepia2">#77390A</div>
    <div class="color-swatch sepia3">#DAC4B0</div>
    <div class="color-swatch sepia4">#C4A48A</div>
```

- `#9F5A2C` – primary sepia tone  
- `#77390A` – heading color  
- `#DAC4B0` – light background / neutral  
- `#C4A48A` – accent / secondary background

**Blue Accent Colors**

```
    <div class="color-swatch accent1">#39BBFF</div>
    <div class="color-swatch accent2">#277DD1</div>
    <div class="color-swatch accent3">#0C61B9</div>
    <div class="color-swatch accent4">#00356B</div>
```

- `#39BBFF` – hyperlink / callout highlight  
- `#277DD1` – secondary hyperlink / buttons  
- `#0C61B9` – tertiary accent  
- `#00356B` – deep accent / headers if needed

## Headings

- All headings should use `#77390A`.  
- Use `=` for top-level (`h1`), `-` for second-level (`h2`), `~` for third-level (`h3`).  
- Keep headings clear and descriptive.

Example:

```
# Section Title

## Subsection Title

### Sub-subsection Title
```


## Text and Typography

- **Body text:** Dark brown or black, high contrast against light sepia backgrounds (`#DAC4B0` or `#C4A48A`).  
- **Links:** Use `#39BBFF` for standard links; hover states can be `#277DD1`.  
- **Emphasis:** Italics or bold as needed, but avoid excessive styling.


## Lists

- Use bullets for unordered lists (`*`), numbers for ordered lists (`1.`).  
- Nested lists are indented by **3 spaces** per level.  

Example:
```
* First item
   * Nested item
* Second item
```


## Callouts / Notes

- Use **blue accents** for informational callouts. Example HTML snippet:

```
    <div style="border-left: 4px solid #39BBFF; padding: 0.5rem; background-color: #DAC4B0;">
    <strong>Note:</strong> This is an informational callout.
    </div>
```

- For warnings or cautions, consider using **sepia2 (#77390A)** for borders with `#DAC4B0` background.


## Images

- Prefer **high-resolution images** and consistent styling.  
- Backgrounds should not clash with sepia tones; transparent backgrounds are ideal.  
- File naming: lowercase, hyphen-separated (see File Naming Conventions).


## Branding Consistency

- Capybara logo should appear in the **top-left** of Read the Docs sidebar.  
- Edition info (name, version, tagline) should appear directly below the logo.  
- Color accents in headings, links, and callouts should match the defined palette.


## Supplemental Guidelines

- Maintain **semantic Markdown / RST** structure for headings, lists, and links.  
- Update the **Style Notes and Guidelines** section whenever a new edition makes a deliberate style change.  
- Preserve **edition metadata** and **author/copyright credit** when creating forks or new versions.

