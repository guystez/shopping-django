# Generated by Django 4.1.5 on 2023-01-09 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0002_cart_cartarchive"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cart", old_name="cartarchive", new_name="in_cart",
        ),
    ]
