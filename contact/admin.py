from django.contrib import admin
from .models import ContactModel
# Register your models here.

class contactadmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'date']
admin.site.register(ContactModel, contactadmin)
