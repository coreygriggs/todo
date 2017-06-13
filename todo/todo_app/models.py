from django.db import models


class ToDo(models.Model):
    """
    todos
    """
    CHOICES = (
        ('open', 'open'),
        ('complete', 'complete')
    )
    name = models.CharField(max_length=256)
    status = models.CharField(max_length=20, choices=CHOICES, default='open')
    todo_list = models.ForeignKey('ToDoList')

class ToDoList(models.Model):
    """
    todo lists for different types of task lists
    """
    name = models.CharField(max_length=256)
    