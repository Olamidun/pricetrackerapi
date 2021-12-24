web: gunicorn ptracker.wsgi

worker: celery -A ptracker worker -l info

beat: celery -A tasks worker -B -l INFO