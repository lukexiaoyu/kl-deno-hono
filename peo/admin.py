from django.contrib import admin
from .models import Peo

@admin.register(Peo)
class PeoAdmin(admin.ModelAdmin):
    list_display=['id','name','age']

# Register your models here.
