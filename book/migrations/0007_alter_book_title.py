# Generated by Django 4.2.13 on 2024-06-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0006_alter_cart_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=50),
        ),
    ]