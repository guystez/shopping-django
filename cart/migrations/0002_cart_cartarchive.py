# Generated by Django 4.1.5 on 2023-01-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="cartarchive",
            field=models.BooleanField(default=False),
        ),
    ]
