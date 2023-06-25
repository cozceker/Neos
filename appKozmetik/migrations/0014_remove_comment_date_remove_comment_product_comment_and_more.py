# Generated by Django 4.2.1 on 2023-06-11 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appKozmetik', '0013_comment_time_alter_comment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='product_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Saat'),
        ),
    ]