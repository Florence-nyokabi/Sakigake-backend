from django.db import models
class CompetencyBasedGrade(models.Model):
    GRADE_CHOICES = (
        (1, 'Grade 1'),
        (2, 'Grade 2'),
        (3, 'Grade 3'),
        (4, 'Grade 4'),
        (5, 'Grade 5'),
        (6, 'Grade 6'),
    )
