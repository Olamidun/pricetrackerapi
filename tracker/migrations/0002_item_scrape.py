# Generated by Django 3.1.1 on 2021-01-28 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='scrape',
            field=models.BooleanField(default=True),
        ),
    ]
