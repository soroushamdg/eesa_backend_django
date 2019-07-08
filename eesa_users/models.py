from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class user_student(models.Model):

    user = models.OneToOneField(User,on_delete=models.PROTECT)
    student_number = models.CharField(max_length=10)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

