from django.db import models
import datetime
# Create your models here.
class teacher(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

class courses_category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


class courses_course(models.Model):

    name = models.CharField(max_length=32)
    teacher = models.ForeignKey(to=teacher,on_delete=models.PROTECT)
    start_date = models.CharField(max_length=32)
    end_date = models.CharField(max_length=32)
    hours_length = models.CharField(max_length=3)
    price = models.CharField(max_length=12)
    evand_link = models.URLField(null=True, blank=True)
    image = models.ImageField(blank=True,null=True,upload_to=f'courses_images/{datetime.datetime.now().strftime("%m/%d/%Y/%H/%M/%S")}')
    # TODO : registered users here connect using foreign keys to Users objects

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Courses'
        verbose_name = 'Course'