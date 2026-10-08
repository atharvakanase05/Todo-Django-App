from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Completed', 'Created_at')
    list_filter = ('Title', 'Completed')
    search_fields = ('Title', 'Completed')
    ordering = ('-Created_at',)