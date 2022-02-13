from django.contrib import admin
from myapp.models import *

# Register your models here.
@admin.register(Secretary)
class AdminSecretary(admin.ModelAdmin):
    list_display=['name','email','phone','address','password','pic']