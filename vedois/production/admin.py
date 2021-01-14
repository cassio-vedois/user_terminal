from django.contrib import admin
from vedois.production import models


# Register your models here.
@admin.register(models.UserTerminal)
class UserTerminalAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']
    ordering = ['username']

