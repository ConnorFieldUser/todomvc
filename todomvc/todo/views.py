# from django.shortcuts import render
from rest_framework.generics import ListAPIView

from todo.models import Todo
from todo.serializers import TodoSerializer

# Create your views here.


class TodoListAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
