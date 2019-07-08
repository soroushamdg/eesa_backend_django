from django.contrib import admin
from eesa_courses import models

# Register your models here.

admin.site.register(models.courses_category)
admin.site.register(models.courses_course)
admin.site.register(models.course_teacher)