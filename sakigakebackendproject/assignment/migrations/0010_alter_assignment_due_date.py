# Generated by Django 4.2.5 on 2023-09-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0009_alter_assignment_category_alter_assignment_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
