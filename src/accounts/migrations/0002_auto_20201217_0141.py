# Generated by Django 3.1.4 on 2020-12-17 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.IntegerField(max_length=11),
        ),
    ]
