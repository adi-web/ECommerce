web: python manage.py makemigrations && python manage.py migrate && python manage.py loaddata myfixture.json && python manage.py collectstatic --noinput && gunicorn Ecommerce_Store.wsgi --log-file -
