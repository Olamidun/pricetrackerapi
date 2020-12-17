from rest_framework import serializers
from .models import Account

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, write_only=True, min_length=8)
    
    class Meta:
        model = Account
        fields = ['username', 'email', 'phone_number', 'password']

        # def validate(self, data):
        #     email = data['email']
        #     username = data['username']
        #     phone = data['phone_number']

        #     if len(password) <= 5:
        #         raise serializers.ValidationError({'Password Error': 'Your password mst be more than 5 characters'})
        #     return data
        
        def create(self, validated_data):
            return Account.objects.create_user(**validated_data)

            