# Generated by Django 5.0.3 on 2024-04-16 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_order_alter_shippingaddress_shipping_address2_and_more'),
        ('product', '0013_alter_category_options_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
