from django.contrib import admin
from .models import UploadedFile


@admin.register(UploadedFile)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')