web: python manage.py makemigrations &&
python manage.py migrate &&
python manage.py collectstatic --noinput &&
 gunicorn django_project.wsgi --log-file -