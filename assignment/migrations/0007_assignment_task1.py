# Generated by Django 3.2.7 on 2023-09-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0006_alter_assignment_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='task1',
            field=models.CharField(default='null', max_length=24),
            preserve_default=False,
        ),
    ]
