from django.db import models

# Create your models here.
class teacher(models.Model):
    name = models.CharField(max_length=32, unique=True)

class courses_category(models.Model):

    name = models.CharField(max_length=32)
    teacher = models.ForeignKey(to=teacher,on_delete=models.PROTECT)
    date = models.DateField()
    hours_length = models.IntegerField()
    price = models.CharField(max_length=12)
    evand_link = models.URLField(null=True,blank=True)
    # TODO : registered users here connect using foreign keys to Users objects

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Courses'
        verbose_name = 'Course'