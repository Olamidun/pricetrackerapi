# Generated by Django 3.1.1 on 2021-01-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
