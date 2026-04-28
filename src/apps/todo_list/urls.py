from django.urls import path
from .views import TodoListCreateView, TodoDetailView, TodoToggleCompleteView

urlpatterns = [
    path("todos/", TodoListCreateView.as_view()),  # no name
    path("todos/<int:pk>/", TodoDetailView.as_view()),  # no name
    path("todos/<int:pk>/toggle/", TodoToggleCompleteView.as_view()),
]
