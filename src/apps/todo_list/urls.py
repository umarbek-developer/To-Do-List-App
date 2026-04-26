from django.urls import path
from .views import (
    TodoListCreateView,
    TodoRetrieveUpdateDestroyView,
    TodoToggleCompleteView,
)

urlpatterns = [
    path('', TodoListCreateView.as_view(), name='todo-list-create'),
    path('<int:pk>/', TodoRetrieveUpdateDestroyView.as_view(), name='todo-detail'),
    path('<int:pk>/toggle/', TodoToggleCompleteView.as_view(), name='todo-toggle'),
]