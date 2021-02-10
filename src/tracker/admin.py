from django.contrib import admin
from tracker.models import Item

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'item_title', 'requested_price', 'last_price', 'scrape', 'date_created']
    list_display_links = ['user', 'item_title',]
    search_fields = ['item_title']


admin.site.register(Item, ItemAdmin)

# admin.site.register(Test)
