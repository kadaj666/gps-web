#!/bin/bash

apt-get update
apt-get install python3-dev -y
pip3 install -r /opt/src/requirements.txt
cd /opt/src
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:9009 &
/bin/bash celery.sh &
/bin/bash
