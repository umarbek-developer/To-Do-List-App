from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.users.models import User
from apps.users.resources import UserResource


@admin.register(User)
class UserModelAdmin(ImportExportModelAdmin):
    list_display = ["first_name", "last_name"]
    resource_class = [UserResource]
