from django.contrib import admin
from .models import Categories, Sessions, Threads, Posts


# Register your models here.

@admin.register(Categories, Sessions, Threads, Posts)
class BaseAdminRegister(admin.ModelAdmin):
    pass
