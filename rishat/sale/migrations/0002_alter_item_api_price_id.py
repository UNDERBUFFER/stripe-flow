# Generated by Django 4.1.1 on 2023-02-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='api_price_id',
            field=models.TextField(default=None, unique=True),
        ),
    ]
