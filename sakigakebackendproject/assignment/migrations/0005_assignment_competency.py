# Generated by Django 4.2.5 on 2023-09-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0004_remove_assignment_competency_assignment_materials'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='competency',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
