# Generated by Django 4.0.5 on 2022-06-27 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('burgerwars', '0004_checkout_remove_item_item_cart_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='cart_address',
            new_name='checkout_address',
        ),
        migrations.RenameField(
            model_name='checkout',
            old_name='cart_customer',
            new_name='checkout_customer',
        ),
        migrations.RenameField(
            model_name='checkout',
            old_name='cart_payment',
            new_name='checkout_payment',
        ),
        migrations.RenameField(
            model_name='checkout',
            old_name='cart_product',
            new_name='checkout_product',
        ),
    ]
