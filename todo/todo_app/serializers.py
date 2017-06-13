from rest_framework import serializers
from .models import ToDoList, ToDo


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('name',)


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('name', 'status', 'todo_list', 'pk',)