# Generated by Django 4.2.4 on 2023-08-02 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_customer_order_product_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='uploads/'),
        ),
    ]
