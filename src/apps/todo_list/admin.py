from django.contrib import admin
from apps.todo_list.models import Todo
from import_export.admin import ImportExportModelAdmin
from apps.todo_list.resources import TodoResource


@admin.register(Todo)
class TodoModelAdmin(ImportExportModelAdmin):
    list_display = ("title", "deadline")
    resource_class = [TodoResource]
