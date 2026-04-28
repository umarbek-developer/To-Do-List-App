from django.contrib import admin
from .models import Todo
from import_export.admin import ImportExportModelAdmin
from .resources import TodoResource


@admin.register(Todo)
class TodoAdmin(ImportExportModelAdmin):  # replaces admin.ModelAdmin
    resource_class = TodoResource
    list_display = ("title", "user", "is_completed", "deadline", "created_at")
    list_filter = ("is_completed",)
