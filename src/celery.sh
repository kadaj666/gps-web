rm -r -f celerybeat.pid
celery -A parser worker -l error -Q parse_market --autoscale=1,4 -n parse_market --pool prefork &
celery -A parser beat -l error --scheduler django_celery_beat.schedulers:DatabaseScheduler &
