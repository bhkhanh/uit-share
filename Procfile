release: python manage.py makemigrations && python manage.py migrate && python manage.py check --deploy
web: gunicorn __core__.wsgi --log-file -