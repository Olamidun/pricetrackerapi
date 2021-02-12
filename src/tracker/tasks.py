import time
from twilio.rest import Client
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
from django.core.exceptions import ValidationError
from .models import Item
from accounts.models import Profile
from .scraper import get_data_from_jumia

def send_sms():
    account_sid = 'AC6c18cd77fd4da2d392f3acdbe8c49808'
    auth_token = '2a2edc0f990a4e98bf8655af4b8117e0'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                body='Hello my nigga',
                from_='+12562865991',
                to='+2348103087162'
            )

    print(message.sid)


@shared_task
def track_for_discount():
    items = Item.objects.all()
    

    for item in items:
        # Crawl item url
        profile = Profile.objects.get(user=item.user)
        try:
            if item.scrape:
                print(item.item_title)
                print(item.scrape)
                data = get_data_from_jumia(item.url)
                last_price = data.get("price", '')
                item.last_price = last_price
                item.save()
                requested_price = item.requested_price

                # print(data)

                if last_price <= requested_price:
                    item.discounted_price = item.discount
                    if profile.notify_by_email and profile.notify_by_sms:
                        subject = f'Dear {item.user.username}, there is a discount of {item.discounted_price} for the {item.item_title} you are tracking, visit {item.url} to purchase it. Thanks for using our platform'
                        send_mail(
                            'Yaay, there is a discount🥳',
                            subject,
                            settings.EMAIL_HOST_USER,
                            [item.user.email]
                        )

                        send_sms()

                    elif not profile.notify_by_email and profile.notify_by_sms:
                        send_sms()
                        
                    # elif profile.notify_by_email and not profile.notify_by_sms:
                        
                    item.scrape = False
                    item.save()
        except ValidationError:
            print('something went wrong, try again!!!!')

while True:
    track_for_discount()
    time.sleep(15)



