# Generated by Django 5.0.3 on 2024-03-31 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyShop', '0002_alter_category_options_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product_images/'),
        ),
    ]