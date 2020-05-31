web: gunicorn golf_society.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate