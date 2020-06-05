web: gunicorn mysite.wsgi --log-file -
main_worker celery -A mysite worker --without-gossip --beat -l info
