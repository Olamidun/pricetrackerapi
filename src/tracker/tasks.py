import time
from django.core.mail import send_mail
from django.conf import settings
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
            if item.scrape:
                print(item.scrape)
                data = get_data_from_jumia(item.url)
                last_price = data.get("price", '')
                item.last_price = last_price
                item.save()
                requested_price = item.requested_price

                # print(data)

                if last_price <= requested_price:
                    send_mail(
                        'Yaay, there is a discount🥳',
                        f'Dear {item.user.email}, it seems there is a discount for the item you are tracking, visit {item.url} to purchase it.',
                        settings.EMAIL_HOST_USER,
                        [item.user.email]
                    )
                    item.scrape = False
                    item.save()
        except ValidationError:
            print('something went wrong, try again!!!!')

while True:
    track_for_discount()
    time.sleep(15)



