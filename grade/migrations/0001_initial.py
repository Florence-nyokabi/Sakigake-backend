# Generated by Django 3.2.7 on 2023-09-27 13:51

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import multiselectfield.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_name', models.CharField(max_length=50)),
                ('subjects', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Math'), ('2', 'English'), ('3', 'Kiswahili'), ('4', 'Science'), ('5', 'Agriculture'), ('6', 'Art & Design')], max_length=11, validators=[multiselectfield.validators.MaxValueMultiFieldValidator(6)])),
                ('class_teacher', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grade', to='teachers.teacher')),
            ],
        ),
    ]