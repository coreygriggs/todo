from rest_framework.test import APITestCase, APIClient
from django.core.urlresolvers import reverse
from .models import ToDoList, ToDo


def create_todolist(name):
    new_list = ToDoList(name=name)
    new_list.save()
    return new_list

class ToDoLists(APITestCase):

    def test_get_todo_lists(self):
        new_list = create_todolist('test_list')
        self.client = APIClient(enforce_csrf_checks=False)
        response = self.client.get(reverse('todo_lists'), format='json')
        self.assertEqual(response.json()[0]['name'], 'test_list')

    def test_post_todo_list(self):
        self.client = APIClient(enforce_csrf_checks=False)
        response = self.client.post(reverse('todo_lists'), data={"name": "Today's todos"}, format='json')
        self.assertEquals(response.json()['name'], "Today's todos")


class Todo(APITestCase):
    
    def test_get_todo(self):
        new_todo_list = create_todolist("Today's list")
        new_todo = ToDo(name='take out trash', todo_list=new_todo_list)
        new_todo.save()
        self.client = APIClient(enforce_csrf_checks=False)
        response = self.client.get(reverse('todos'), format='json')
        self.assertEqual(response.json()[0]['name'], 'take out trash')

