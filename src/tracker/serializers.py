from tracker.models import Item
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user')
    class Meta:
        model = Item
        fields = ['user', 'item_title','url', 'requested_price', 'last_price', 'discounted_price']
        extra_kwargs = {
            "discounted_price": {
                "required": False,
            }
        }

    
    def get_user(self, item):
        user = item.user.username
        return user