from django.db import models


class ToDo(models.Model):
    """
    todos
    """
    TODO_STATUSES = (
        ('complete', 'complete'),
        ('open', 'open'),
    )
    name = models.CharField(max_length=256)
    status = models.CharField(max_length=2, choices=TODO_STATUSES)

class ToDoList(models.Model):
    """
    todo lists for different types of task lists
    """
    name = models.CharField(max_length=256)

class ListToDos(models.Model):
    """
    relational table of todo lists and todos
    """
    todo = models.ForeignKey('ToDo')
    todo_list = models.ForeignKey('ToDoList')
    