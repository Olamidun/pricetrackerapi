# from celery import shared_task

# from celery.decorators import periodic_task
# from celery.task.schedules import crontab

# from .models import Test



# @shared_task
# def create_test_object(name, code):
#     Test.objects.create(name=name, code=code)


# @periodic_task(run_every=(crontab(minute='*/1')))
# def run_create_test_object():
#     create_test_object.delay('Kolapo', 'abcd123efg')


