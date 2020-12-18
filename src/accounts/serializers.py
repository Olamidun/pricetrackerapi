from rest_framework import serializers
from .models import Auth
from django.db.models.signals import pre_save

class RegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(max_length=60, write_only=True, min_length=8)
    
    class Meta:
        model = Auth
        fields = ['username', 'email', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        # def validate(self, data):
        #     email = data['email']
        #     username = data['username']
        #     phone = data['phone_number']

        #     if len(password) <= 5:
        #         raise serializers.ValidationError({'Password Error': 'Your password mst be more than 5 characters'})
        #     return data
        
        def create(self, validated_data):
            password_ = validated_data.get('password', None)
            user = Auth.objects.create_user(
                username = validated_data['username'],
                email = validated_data['email'],
                phone_number = validated_data['phone_number']
            )
            return user

        # function to hash password
        def create_hash(sender, instance=None, *args, **kwargs):
            passwd = instance.password
            instance.set_password(passwd)

        pre_save.connect(create_hash, sender=Auth)

            