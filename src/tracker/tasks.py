import time
from celery import shared_task
from django.core.exceptions import ValidationError
from .models import Item
from .scraper import get_data_from_jumia


@shared_task
def track_for_discount():
    items = Item.objects.all()

    for item in items:
        # Crawl item url
        try:
            data = get_data_from_jumia(item.url)
            last_price = data.get("price", '')
            requested_price = item.requested_price
            print(data)

            if last_price <= requested_price:
                print('Yaaaay, there is a discount for you!!')
        except ValidationError:
            print('something went wrong, try again!!!!')

while True:
    track_for_discount()
    time.sleep(15)


    


# @periodic_task(run_every=(crontab(minute='*/1')))
# def run_create_test_object():
#     create_test_object.delay('Kolapo', 'abcd123efg')


