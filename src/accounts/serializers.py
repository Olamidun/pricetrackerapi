from rest_framework import serializers
from .models import Account, Profile
from django.db.models.signals import pre_save

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, write_only=True, min_length=8)
    
    class Meta:
        model = Account
        fields = ['username', 'email', 'phone_number', 'password']
        
        def create(self, validated_data):
            password_ = validated_data.get('password', None)
            user = Account.objects.create_user(
                username = validated_data['username'],
                email = validated_data['email'],
                phone_number = validated_data['phone_number']
            )
            return user

        # function to hash password
        def create_hash(sender, instance=None, *args, **kwargs):
            passwd = instance.password
            instance.set_password(passwd)

        pre_save.connect(create_hash, sender=Account)


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_username')
    class Meta:
        model = Profile
        fields = ['user', 'notify_by_email', 'notify_by_sms',]

        
    def get_username(self, profile):
        user = profile.user.username
        return user
