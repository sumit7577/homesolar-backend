from django.contrib import admin
from app.models import *
# Register your models here.

class EmailAdmin(admin.ModelAdmin):
    model = Email
    list_display = ("id", "name","email")


admin.site.register(Email,EmailAdmin)
