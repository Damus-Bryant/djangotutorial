# Django Polls Tutorial (Django 5.2)

A learning project following Django’s official tutorial (Parts 1–8), with:
- Polls app (vote on questions, results)
- Admin customizations (inline choices, filters, search)
- Basic tests (models + views)
- Django Debug Toolbar for development

## Requirements
- Python 3.10+ (tested on 3.13)
- Django 5.2.x

**Optional (dev):**
- `django-debug-toolbar`

## Quick Start (Windows)

```bat
git clone https://github.com/Damus-Bryant/djangotutorial.git
cd djangotutorial

:: (optional) create a venv
py -m venv .venv
.\.venv\Scriptsctivate

:: install deps
py -m pip install -U pip
py -m pip install "django==5.2.*" django-debug-toolbar

:: setup DB
py manage.py migrate
py manage.py createsuperuser

:: run
py manage.py runserver
```

Open:
- App: <http://127.0.0.1:8000/polls/>
- Admin: <http://127.0.0.1:8000/admin/>

## Running Tests
```bat
py manage.py test polls
```

## Debug Toolbar (dev only)
Add to `INSTALLED_APPS` and `MIDDLEWARE`, set `INTERNAL_IPS=["127.0.0.1"]`, and keep `DEBUG=True`.  
Toggle with:
```python
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}
```

## Admin Extras
- Inline `Choice` rows on the `Question` page
- Columns: *Question text*, *Date published*, *Published recently?*
- Filters, search, ordering, date hierarchy
- Simple branding via `admin.site.site_header`, etc.

## Project Structure (short)
```
djangotutorial/
  manage.py
  mysite/
    settings.py
    urls.py
  polls/
    admin.py
    models.py
    tests.py
    urls.py
    views.py
    templates/polls/
      index.html
      detail.html
      results.html
    static/polls/
      styles.css
      images/background.png
```

## Notes / Security
- Tutorial app — not production-ready.
- **Do not commit secrets.** Move `SECRET_KEY` to env vars for public repos.
- For production: set `DEBUG=False`, configure `ALLOWED_HOSTS`, and serve static files properly (e.g., WhiteNoise).

## License
MIT/BSD recommended for examples. Add a `LICENSE` file if you plan to share.
