# Generated by Django 4.2.1 on 2023-06-10 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appKozmetik', '0008_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]