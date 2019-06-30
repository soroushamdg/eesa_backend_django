from django.contrib import admin

# Register your models here.
from eesa_main import models

admin.site.register(models.eesa_team_member)
admin.site.register(models.eesa_information)