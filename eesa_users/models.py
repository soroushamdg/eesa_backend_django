from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Student(models.Model):

    user = models.OneToOneField(User,on_delete=models.PROTECT)

    student = models.CharField(max_length=10)
    name = models.CharField(max_length=60)