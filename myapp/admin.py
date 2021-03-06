from django.contrib import admin
from myapp.models import *

# Register your models here.
@admin.register(Secretary)
class AdminSecretary(admin.ModelAdmin):
    list_display=['name','email','phone','address','password','pic']



@admin.register(House)
class AdminHouse(admin.ModelAdmin):
    list_display=['room_no','image']



@admin.register(Member)
class AdminMember(admin.ModelAdmin):
    list_display=['name','email','phone','password','doc','doc_number','address','pic']



@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','contact_no']



@admin.register(Gallery)
class AdminGallery(admin.ModelAdmin):
    list_display = ['name','image']



@admin.register(Notice)
class AdminNotice(admin.ModelAdmin):
    list_display = ['subject','date','notice']