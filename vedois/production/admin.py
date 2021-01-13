from django.contrib import admin
from vedois.production import models


# Register your models here.
@admin.register(models.UserTerminal)
class UserTerminalAdmin(admin.ModelAdmin):
    list_display = ['username']
    ordering = ['username']

