# Generated by Django 4.2.5 on 2023-09-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_alter_subject_subject_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(choices=[('English', 'English'), ('Kiswahili', 'Kiswahili'), ('Mathematics', 'Mathematics'), ('Integrated Science', 'Integrated Science'), ('Social Studies', 'Social Studies')], max_length=100),
        ),
    ]
