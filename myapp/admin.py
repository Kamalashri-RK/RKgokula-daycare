from django.contrib import admin
from .models import AdmissionEnquiry

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('parent_name','phone','child_name','age_group','city','created_at')

admin.site.register(AdmissionEnquiry, AdmissionAdmin)
