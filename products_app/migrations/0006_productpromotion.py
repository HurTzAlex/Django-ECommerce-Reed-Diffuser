# Generated by Django 4.2.7 on 2024-01-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0005_delete_productpromotion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPromotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagePromotion', models.ImageField(upload_to='products-promotion-img')),
                ('namePromotion', models.CharField(max_length=50)),
            ],
        ),
    ]
