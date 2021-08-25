from django.contrib import admin
from .models import Jobs

# Register your models here.
@admin.register(Jobs)
class JobAdmin(admin.ModelAdmin):
    pass
