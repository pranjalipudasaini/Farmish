# Generated by Django 5.0.3 on 2024-04-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_created_at_product_listed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='lifespan',
            field=models.IntegerField(default=0, help_text='Lifespan in days'),
        ),
    ]
