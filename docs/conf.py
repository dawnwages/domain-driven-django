# Sphinx configuration for the Domain-Driven Django book site.

project = "Domain Driven Django"
author = "Dawn Wages"
copyright = "2024, Dawn Wages"

extensions = ["sphinx_copybutton"]

templates_path = ["_templates"]
exclude_patterns = ["_build"]

html_theme = "furo"
html_title = "Domain Driven Django"
html_static_path = ["_static"]
html_css_files = [
    "https://fonts.googleapis.com/css2?family=Lexend:wght@400;600;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap",
    "custom.css",
]
html_favicon = "_static/img/favicon-32x32.png"
html_show_sourcelink = False
html_baseurl = "https://dawnwages.github.io/domain-driven-django/"

# Colors pulled from the header illustration.
html_theme_options = {
    "source_repository": "https://github.com/dawnwages/domain-driven-django/",
    "source_branch": "main",
    "source_directory": "docs/",
    "light_css_variables": {
        "color-brand-primary": "#8a2fb3",
        "color-brand-content": "#8a2fb3",
        "color-brand-visited": "#6f2590",
        "font-stack": "'Source Serif 4', Georgia, serif",
        "font-stack--headings": "Lexend, system-ui, sans-serif",
    },
    "dark_css_variables": {
        "color-brand-primary": "#d59cf0",
        "color-brand-content": "#d59cf0",
        "color-brand-visited": "#c083dd",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/dawnwages/domain-driven-django",
            "html": '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>',
            "class": "",
        },
    ],
}

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/subscribe.html",
        "sidebar/scroll-end.html",
    ]
}
