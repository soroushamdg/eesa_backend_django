from django.contrib import admin
from eesa_sci_center.models import scicenter_category,scicenter_writer,scicenter_document,scicenter_project,scicenter_tutorial
# Register your models here.
admin.site.register(scicenter_category)
admin.site.register(scicenter_writer)
admin.site.register(scicenter_document)
admin.site.register(scicenter_project)
admin.site.register(scicenter_tutorial)