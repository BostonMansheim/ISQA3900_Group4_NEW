# Generated by Django 4.0.5 on 2022-06-27 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('burgerwars', '0003_remove_item_topping_item_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='burgerwars.address')),
                ('cart_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='burgerwars.customer')),
                ('cart_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='burgerwars.payment')),
                ('cart_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='burgerwars.product')),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_cart',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]