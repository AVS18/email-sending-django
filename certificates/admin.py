from django.contrib import admin
from .models import Email
# Register your models here.
class EmailRef(admin.ModelAdmin):
    list_display=['par_name','par_email','par_event']
    list_filter=['par_event']

admin.site.register(Email,EmailRef)
