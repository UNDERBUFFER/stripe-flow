# Generated by Django 4.1.1 on 2023-02-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_alter_item_api_price_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='api_price_id',
            field=models.TextField(blank=True, default=None, null=True, unique=True),
        ),
    ]
