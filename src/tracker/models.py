from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

# Create your models here.

User = settings.AUTH_USER_MODEL

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_title = models.CharField(max_length=300, null=True, blank=True)
    url = models.URLField()
    item_image_url = models.URLField(null=True, blank=True)
    requested_price = models.FloatField(default=0)
    last_price = models.FloatField(null=True, blank=True)
    discounted_price = models.FloatField(null=True, blank=True)
    scrape = models.BooleanField(default=True)

    def amount_saved(self):
        amount = self.last_price - self.discounted_price
        return amount

    def __str__(self):
        return f"{self.user.username}'s {self.item_title}"



# class Test(models.Model):
#     name = models.CharField(max_length=300)
#     code = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name