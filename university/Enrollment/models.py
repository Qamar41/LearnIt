from django.db import models
from datetime import datetime
# Create your models here.


class Enrollment(models.Model):
    course=models.CharField(max_length=200)
    course_id=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=100)
    enroll_Date=models.DateTimeField(default=datetime.now, blank=True)
    user_id=models.IntegerField(blank=True)

    def __str__(self):
        return self.name

