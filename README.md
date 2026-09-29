# domain-driven-django
Django in Domain Driven Design: How do you leverage the opinions of the framework to handle technical nuances, and structure business logic for easier refactoring with your domain-experts.

Read it at https://dawnwages.github.io/domain-driven-django/

## Writing

The site is built with [Sphinx](https://www.sphinx-doc.org/) and the [Furo](https://pradyunsg.me/furo/) theme.

- Chapters live in `docs/posts/*.rst`; add new ones to the `toctree` in `docs/index.rst`.
- Brand styles are in `docs/_static/custom.css`.
- The newsletter signup (`docs/_templates/sidebar/subscribe.html`) and giscus comments (`docs/_templates/page.html`) are added to every page automatically.

Pushing to `main` builds the site and deploys it to GitHub Pages (`.github/workflows/static.yml`).

## Developer path

This project uses [uv](https://docs.astral.sh/uv/):

- Python is installed and managed by uv, pinned in `.python-version`.
- One virtual environment, `.venv`, created by `uv sync` (or `uv venv`).
- Dependencies are pinned in `pyproject.toml` / `uv.lock`; add packages with `uv add --group docs <pkg>` (uv environments have no `pip`, so "No module named pip" is expected).
- Run commands with `uv run ...` or after `source .venv/bin/activate`.

Build and preview locally:

```bash
uv run sphinx-build -b html docs _build/html
```

```bash
uv run python -m http.server 8765 -d _build/html
```
