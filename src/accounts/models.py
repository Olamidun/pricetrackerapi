from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, username, email, phone_number, password=None):
        if username is None:
            raise TypeError('Users must have a username')
        if email is None:
            raise TypeError('Users must supply email')
        if phone_number is None:
            raise TypeError('Users must supply a phone_number')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            phone_number = phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password):
        user = self.create_user(username, email, phone_number, password)
        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_verified = True
        user.save(using=self._db)
        return user

    
class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.BigIntegerField()
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    objects = AccountManager()

    def __str__(self):
        return self.username



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    notify_by_email = models.BooleanField(default=True)
    notify_by_sms = models.BooleanField(default=False)
    notify_by_whatsapp = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username