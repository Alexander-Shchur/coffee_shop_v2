from django.contrib import admin
from core.models import *


# Register your models here.
@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = [
        i for i in Coffee.__dict__
    ]
