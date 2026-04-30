from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from apps.todo_list.serializers import (
    TodoCreateSerializer,
    TodoUpdateSerializer,
    TodoListSerializer,
)
from apps.todo_list.models import Todo


class TodoListApiView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer


class TodoCreateApiView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer


class TodoUpdateApiView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoUpdateSerializer


class TodoDestoryApiView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
