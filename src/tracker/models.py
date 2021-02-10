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
    date_created = models.DateTimeField(auto_now_add=True)


    @property
    def discount(self):
        if self.last_price <= self.requested_price:
            discount_amount = self.requested_price - self.last_price
        else:
            discunt_amount = 0

        return amount

    def __str__(self):
        return f"{self.user.username}'s {self.item_title}"

