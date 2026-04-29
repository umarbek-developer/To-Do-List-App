from rest_framework.serializers import ModelSerializer
from apps.todo_list.models import Todo


class TodoListSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class TodoCreateSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"



class TodoUpdateSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

