from tracker.models import Item
from rest_framework import serializers
from tracker.scraper import get_data_from_jumia


class ItemSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user')
    class Meta:
        model = Item 
        fields = ['id', 'user', 'item_title', 'item_image_url', 'url', 'requested_price', 'last_price', 'discounted_price', 'scrape']
        extra_kwargs = {
            "discounted_price": {
                "required": False,
            },
            'id':{
                "read_only": True
            }
        }
    
    def get_logged_in_user(self):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            return request.user
        return None

    def create(self, validated_data):
        user = self.get_logged_in_user()
        if Item.objects.filter(user=user, url=validated_data['url']).exists():
            raise serializers.ValidationError({'error': "This URL already exist, you do not have to add it again, the website is already tracking the item for you."})

        try:
            jumia_data = get_data_from_jumia(validated_data['url'])
            validated_data['last_price'] = jumia_data['price']
            validated_data['item_title'] = jumia_data['title']
            validated_data['item_image_url'] = jumia_data['image']
        except:
            raise serializers.ValidationError({'error': "Please confirm that the url you entered exists and that you have stable internet conncetion"})

        

        if validated_data['last_price'] < validated_data['requested_price']:
            validated_data['discounted_price'] = validated_data['requested_price'] - validated_data['last_price']
            item = Item.objects.create(**validated_data)
            return item
        item = Item.objects.create(**validated_data)
        item.scrape = True
        item.save()
        return item

    
    def update(self, instance, validated_data):
        instance.requested_price = validated_data.get('requested_price', instance.requested_price)

        if instance.last_price <= instance.requested_price:
            instance.discounted_price = instance.requested_price - instance.last_price
        instance.scrape = validated_data.get('scrape', instance.scrape)
        instance.save()
        return instance
    
    def get_user(self, item):
        user = item.user.username
        return user


