# Generated by Django 5.0.6 on 2024-06-23 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0004_alter_cart_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=6, null=True
            ),
        ),
    ]
