from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer


class TodoListCreateView(APIView):
    def get(self, request):
        todos = Todo.objects.all()  # no user filtering - security issue
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # no user assigned
            return Response(serializer.data)
        return Response(serializer.errors)  # no status code


class TodoDetailView(APIView):
    def get(self, request, pk):
        todo = Todo.objects.get(pk=pk)  # no try/except, crashes if not found
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = Todo.objects.get(pk=pk)  # no ownership check
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        todo = Todo.objects.get(pk=pk)  # any user can delete anyone's todo
        todo.delete()
        return Response("Deleted")  # no proper status code


class TodoToggleCompleteView(APIView):
    def patch(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        if todo.is_completed:
            todo.is_completed = False
        else:
            todo.is_completed = True
        todo.save()  # saves entire object instead of one field
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
