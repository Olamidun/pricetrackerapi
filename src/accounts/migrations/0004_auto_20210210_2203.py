# Generated by Django 3.1.1 on 2021-02-10 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='notify_by_sms',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='notify_by_whatsapp',
        ),
    ]
