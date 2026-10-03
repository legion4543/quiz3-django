# Quiz 3 – Django: Model → View → URL → Template

A small Django app that lists `Student` records from the database on a styled page.

## Flow

1. `main/models.py` defines `Student`
2. `main/views.py` fetches `Student.objects.all()`
3. `main/urls.py` maps `""` to the `home` view, and `config/urls.py` includes it
4. `main/templates/main/home.html` renders the students

## Run locally (Windows)

Unzip, open the `quiz3_django` folder in VS Code, then in the terminal:

```
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py loaddata students
python manage.py createsuperuser
python manage.py runserver
```

- Home page: http://127.0.0.1:8000/
- Admin (add/edit students): http://127.0.0.1:8000/admin/

`loaddata students` adds 3 sample students. Optional checks: `python manage.py check` and `python manage.py test`.

## GitHub

```
git init
git add .
git commit -m "Quiz 3 Django app"
git branch -M main
git remote add origin https://github.com/<your-username>/quiz3-django.git
git push -u origin main
```

`.gitignore` already excludes `venv/` and `db.sqlite3`.

## PythonAnywhere

1. In a Bash console: `git clone https://github.com/<your-username>/quiz3-django.git`
2. `cd quiz3-django`, then `mkvirtualenv --python=python3.10 venv` and `pip install django`
3. `python manage.py migrate`, `python manage.py loaddata students`, `python manage.py createsuperuser`, `python manage.py collectstatic`
4. Web tab → Add a new web app → Manual configuration (pick the same Python version as your virtualenv)
5. Set Source code and Working directory to `/home/<username>/quiz3-django`, and Virtualenv to `/home/<username>/.virtualenvs/venv`
6. Static files: URL `/static/` → Directory `/home/<username>/quiz3-django/staticfiles` (this makes the admin page look right)
7. Edit the WSGI file: add `/home/<username>/quiz3-django` to `sys.path`, set `os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'`, and use `from django.core.wsgi import get_wsgi_application`
8. Press Reload. `ALLOWED_HOSTS` already allows `*.pythonanywhere.com`.
