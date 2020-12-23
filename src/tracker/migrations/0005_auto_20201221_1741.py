# Generated by Django 3.1.1 on 2020-12-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20201219_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='last_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]