# Generated by Django 3.2.7 on 2023-09-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='is_class_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
