from django.db import models

class Todo(models.Model):
    TODO_STATUSES = (
        ('no', 'Not Started'),
        ('in', 'In Progress'),
        ('co', 'Completed'),
    )

    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=TODO_STATUSES)
