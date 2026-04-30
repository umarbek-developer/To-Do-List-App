from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/todo/", include("apps.todo_list.urls")),
    path("api/user/", include("apps.users.urls")),
]
