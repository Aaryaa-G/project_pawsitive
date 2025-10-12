# Pawsitive

Pawsitive is a small Django-based web project for pet adoption and related pages. This repository contains the Django app code, templates, static assets, and example blog pages.

## Project layout

- `pawsitive/` - Django project module (settings, wsgi, urls, asgi)
- `pawsitive/adoptions/` - Django app for adoptions (models, views, templates, static files)
- `blog/` - static blog pages and templates
- `intlTelInput/` - third-party JS/CSS for phone input
- `pawsitive/media/` - user-uploaded files and pet photos (example subfolders included)
- `db.sqlite3` - SQLite database (example/testing)

## Requirements

- Python 3.8+ (3.10+ recommended)
- pip
- A virtual environment tool (venv, virtualenv, or similar)

## Setup (development)

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies. If a `requirements.txt` exists at the repo root, run:

```powershell
pip install -r requirements.txt
```

If there's no `requirements.txt`, install Django at minimum:

```powershell
pip install django
```

3. Apply migrations and create a superuser (optional):

```powershell
python pawsitive/manage.py migrate
python pawsitive/manage.py createsuperuser
```

4. Run the development server:

```powershell
python pawsitive/manage.py runserver
```

5. Open your browser at `http://127.0.0.1:8000/`.

## Static and media files

- Static files for the `adoptions` app live under `pawsitive/adoptions/static/adoptions/`.
- Media uploads are stored in `pawsitive/media/` (check `pawsitive/settings.py` for MEDIA_ROOT/MEDIA_URL).

If static files are not served automatically in development, run:

```powershell
python pawsitive/manage.py collectstatic
```

## Notes

- This repository contains an example SQLite database `db.sqlite3`. Remove it and rerun migrations for a fresh DB.
- The `intlTelInput` folder contains an included phone input library used by the forms.
- Templates for adoption forms are under `pawsitive/adoptions/templates/adoptions/`.

## Testing

Run tests (if present) with:

```powershell
python pawsitive/manage.py test
```
