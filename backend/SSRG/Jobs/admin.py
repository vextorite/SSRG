from django.contrib import admin
from .models import Jobs, SingleFiles

# Register your models here.
@admin.register(Jobs)
class JobAdmin(admin.ModelAdmin):
    pass
@admin.register(SingleFiles)
class FileAdmin(admin.ModelAdmin):
    pass