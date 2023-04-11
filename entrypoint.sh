#!/bin/sh

# Install packages
RUN pip3 install -r requirements.txt

python manage.py makemigrations --no-input

python manage.py migrate --run-syncdb

python manage.py collectstatic --no-input

#create superuser
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

#run project using gunicorn
gunicorn blog_project.wsgi --bind 0.0.0.0:8000