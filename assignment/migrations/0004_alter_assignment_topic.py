# Generated by Django 3.2.7 on 2023-09-29 06:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0003_alter_assignment_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='topic',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None),
        ),
    ]
