from django.contrib import admin
from boats_auth import models

admin.site.register(models.VisitingDate)
admin.site.register(models.VisitingIP)
admin.site.register(models.Visitor)
