from django.db import models
import datetime
# Create your models here.
class scicenter_category(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Science Center Category"
        verbose_name_plural = 'Science Center Categories'

    def __str__(self):
        return f'{self.id}. {self.name}'

class scicenter_writer(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Science Center writer"
        verbose_name_plural = 'Science Center writers'

    def __str__(self):
        return f'{self.id}. {self.name}'

class scicenter_document(models.Model):
    name = models.CharField(max_length=30)
    issue_date = models.DateField(auto_now=True)
    category = models.ManyToManyField(
        'scicenter_category',
        related_name='scicenter_document_category',
        max_length=5
    )
    writer = models.ManyToManyField(
        'scicenter_writer',
        related_name='scicenter_document_writer',
        max_length=2
    )
    pages = models.CharField(max_length=4, blank=True,null=True)
    is_document_url = models.BooleanField()
    document_file = models.FileField(upload_to=f'scicenter/documents/{datetime.datetime.now().strftime("%m/%d/%Y/%H/%M/%S")}', blank=True,null=True)
    document_url = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name


class scicenter_project(models.Model):
    name = models.CharField(max_length=30)
    issue_date = models.DateField(auto_now=True)
    category = models.ManyToManyField(
        'scicenter_category',
        related_name='scicenter_project_category',
        max_length=5
    )
    writer = models.ManyToManyField(
        'scicenter_writer',
        related_name='scicenter_project_writer',
        max_length=2
    )
    pages = models.CharField(max_length=4, blank=True, null=True)
    is_document_url = models.BooleanField()
    document_file = models.FileField(
        upload_to=f'scicenter/documents/{datetime.datetime.now().strftime("%m/%d/%Y/%H/%M/%S")}', blank=True, null=True)
    document_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class scicenter_tutorial(models.Model):
    name = models.CharField(max_length=30)
    issue_date = models.DateField(auto_now=True)
    category = models.ManyToManyField(
        'scicenter_category',
        related_name='scicenter_tutorial_category',
        max_length=5
    )
    writer = models.ManyToManyField(
        'scicenter_writer',
        related_name='scicenter_tutorial_writer',
        max_length=2
    )
    pages = models.CharField(max_length=4, blank=True, null=True)
    is_document_url = models.BooleanField()
    document_file = models.FileField(
        upload_to=f'scicenter/documents/{datetime.datetime.now().strftime("%m/%d/%Y/%H/%M/%S")}', blank=True, null=True)
    document_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name