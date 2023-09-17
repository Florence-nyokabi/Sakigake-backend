from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from school.models import School

from subject.models import Subject



class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE,null=True)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True)
    password = models.CharField(max_length=255)
    is_class_teacher = models.BooleanField(default=False) 
    date_added_at = models.DateTimeField(auto_now_add=True, verbose_name="Date_Added")
    date_updated_at = models.DateTimeField(auto_now=True, verbose_name="Date_Updated")
    

    def __str__(self):
        return self.first_name