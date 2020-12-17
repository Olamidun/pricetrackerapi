from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class AuthManager(BaseUserManager):
    def create_user(self, username, email, phone_number, password=None):
        if username is None:
            raise TypeError("Users shold have a username")
        if email is None:
            raise TypeError("Users shold have an email")
        if phone_number is None:
            raise TypeError('Users must set a phone number')
        user = self.model(
            username=username,
            phone_number=phone_number,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password):
        user = self.create_user(username, email, phone_number, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.is_verified = True
        user.save(using=self._db)
        return user



class Auth(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    phone_number = models.IntegerField() 
    email = models.EmailField(max_length=255, unique=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    objects = AuthManager()

    def __str__(self):
        return self.username

    

