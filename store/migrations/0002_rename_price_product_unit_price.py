# Generated by Django 5.1.2 on 2024-10-23 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="price",
            new_name="unit_price",
        ),
    ]
