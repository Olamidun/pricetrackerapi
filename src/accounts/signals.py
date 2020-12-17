# imports for signals to create token
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import Auth


# function to create tokens for new users
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


for user in Account.objects.all():
    Token.objects.get_or_create(user=user)

def create_hash(sender, instance=None, *args, **kwargs):
    passwd = instance.password
    instance.set_password(passwd)


pre_save.connect(create_hash, sender=settings.AUTH_USER_MODEL)