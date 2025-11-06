# AgroPredict — Landing (Django)

Landing promocional de AgroPredict tipo “afiche interactivo” para Feria de Software Viña 2025.

## Desarrollo

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # y edita valores si quieres
python manage.py collectstatic --noinput
python manage.py runserver
```

## Deploy (Railway)

1. Sube este repo a GitHub.
2. En Railway: New Project → Deploy from GitHub → selecciona el repo.
3. Variables de entorno (Settings → Variables):
   - `SECRET_KEY` (segura)
   - `DEBUG` = `False`
   - `ALLOWED_HOSTS` = `.railway.app,tu-dominio.cl,localhost,127.0.0.1`
   - `CSRF_TRUSTED_ORIGINS` = `https://*.railway.app,https://tu-dominio.cl`
   - + las de branding/links si quieres personalizar
4. Deploy. Railway ejecuta: `web: gunicorn agropredict_site.wsgi`.
5. Correr `python manage.py collectstatic --noinput` desde Shell en Railway (o post-deploy).
```

## Estructura
```
agropredict-site/
├─ Procfile
├─ README.md
├─ requirements.txt
├─ runtime.txt
├─ .env.example
├─ manage.py
├─ agropredict_site/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
└─ sitepromo/
   ├─ __init__.py
   ├─ apps.py
   ├─ urls.py
   ├─ views.py
   ├─ context.py
   ├─ static/
   │  ├─ sitepromo/
   │  │  ├─ css/styles.css
   │  │  ├─ img/logo-agropredict.svg
   │  │  └─ img/og-cover.jpg
   └─ templates/
      └─ sitepromo/
         ├─ base.html
         ├─ home.html
         └─ legal.html
```
