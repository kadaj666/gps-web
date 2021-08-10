#!/bin/bash

apt-get update
apt-get install python3-dev -y
pip3 install -r /opt/src/requirements.txt
cd /opt/src
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell
python manage.py runserver 0.0.0.0:9009 &
/bin/bash celery.sh &
/bin/bash
