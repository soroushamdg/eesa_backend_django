from django.db import models

# Create your models here.
class eesa_team_member(models.Model):
    name = models.CharField(max_length=40)
    position = models.CharField(max_length=15)
    active_years = models.IntegerField(blank = True,null=True)
    studying_subject = models.CharField(max_length=15)
    image = models.ImageField(blank=True,null = True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name ='Team Member'
        verbose_name_plural = 'Team Members'

class eesa_information(models.Model):
    introduction = models.TextField()
    activities = models.TextField()
    logo = models.ImageField(null=True,blank=True)
    issue_date = models.DateField()
    phone_1 = models.CharField(max_length=15,default=None)
    phone_2 = models.CharField(max_length=15,default=None)
    phone_3 = models.CharField(max_length=15,default=None)
    email = models.CharField(max_length=15,default=None)
    instagram = models.CharField(max_length=25,default=None)
    telegram = models.CharField(max_length=25,default=None)


    def __str__(self):
        return self.issue_date.day, self.issue_date.month, self.issue_date.year