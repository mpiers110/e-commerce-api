# Generated by Django 4.2 on 2023-12-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
