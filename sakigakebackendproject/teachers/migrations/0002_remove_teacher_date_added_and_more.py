# Generated by Django 4.2.5 on 2023-09-11 05:33

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='date_updated',
        ),
        migrations.AddField(
            model_name='teacher',
            name='date_added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date_Added'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='date_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Date_Updated'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
