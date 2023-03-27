from django.contrib import admin

# Register your models here.
from work_app import models

admin.site.register(models.Login)
admin.site.register(models.Workrequest)
admin.site.register(models.Review)
admin.site.register(models.Youtube_link)
