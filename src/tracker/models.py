from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_title = models.CharField(max_length=300)
    url = models.URLField()
    requested_price = models.FloatField()
    last_price = models.FloatField()
    discounted_price = models.FloatField(null=True, blank=True)

    def amount_saved(self):
        amount = self.last_price - self.discounted_price
        return amount

    def __str__(self):
        return f"{self.user.username}'s {self.item_title} tracks"