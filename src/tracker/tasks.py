import os
import time
from twilio.rest import Client
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
from django.core.exceptions import ValidationError
from .models import Item
# from accounts.models import Profile
from .scraper import get_data_from_jumia

# def send_sms(_name, _price, _title, _url, phone):
#     formatted_phone_number = str(phone)
#     account_sid = os.getenv('ACCOUNT_SID')
#     auth_token = os.getenv('AUTH_TOKEN')
#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#                 body='Hello my nigga',
#                 from_=f'Dear {_name}, there is a discount of {_price} for the {_title} you are tracking, visit {_url} to purchase it. Thanks for using our platform',
#                 to=f'+234{formatted_phone_number}'
#             )

#     print(message.sid)


def send_email(name, price, title, item_url, _email):
    subject = f'Dear {name}, \n\n There is a discount of NGN{price} for the {title} you are tracking, visit {item_url} to purchase it. \n\nThank you for using our platform. \n\n Regards, \nTrackforme Team.'
    send_mail(
        'Yaay, there is a discount🥳',
        subject,
        settings.EMAIL_HOST_USER,
        [_email]
    )

@shared_task
def track_for_discount():
    items = Item.objects.all()
    for item in items:
        # Crawl item url
        try:
            if item.scrape:
                print(item.item_title)
                print(item.scrape)
                data = get_data_from_jumia(item.url)
                last_price = data.get("price", '')
                item.last_price = last_price
                item.save()
                requested_price = item.requested_price

                if last_price <= requested_price:
                    item.discounted_price = item.discount
                    send_email(item.user.username, item.discounted_price, item.item_title, item.url, item.user.email)
                       
                    item.scrape = False
                    item.save()
        except ValidationError:
            print('something went wrong, try again!!!!')

while True:
    track_for_discount()
    time.sleep(15)



