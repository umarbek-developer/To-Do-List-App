from django.urls import path
from apps.todo_list.views import (
    TodoListApiView,
    TodoDestoryApiView,
    TodoCreateApiView,
    TodoUpdateApiView,
)

urlpatterns = [
    path("list/", TodoListApiView.as_view()),
    path("create/", TodoCreateApiView.as_view()),
    path("update/<int:pk>", TodoUpdateApiView.as_view()),
    path("delete/<int:pk>", TodoDestoryApiView.as_view()),
]
