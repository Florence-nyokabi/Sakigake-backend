# Generated by Django 3.2.7 on 2023-09-17 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='category',
        ),
    ]