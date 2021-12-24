web: gunicorn ptracker.wsgi

worker: celery -A ptracker worker -l info 

celery -A tasks worker -B -l INFO