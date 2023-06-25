# Generated by Django 4.2.1 on 2023-05-27 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appKozmetik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ürünün fiyatı'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_detail',
            field=models.TextField(blank=True, null=True, verbose_name='Ürünün açıklaması'),
        ),
    ]