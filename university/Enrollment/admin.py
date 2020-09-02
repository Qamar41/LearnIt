from django.contrib import admin
from .models import Enrollment
# Register your models here.

class EnollmentAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'email','course','enroll_Date'
    ]

admin.site.register(Enrollment,EnollmentAdmin)