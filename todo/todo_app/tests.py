from rest_framework.test import APITestCase, APIClient
from django.core.urlresolvers import reverse
from .models import ToDoList, ToDo


def create_todolist(name):
    new_list = ToDoList(name=name)
    new_list.save()
    return new_list

def get_todo_list(pk):
    todo_list = ToDoList.objects.get(pk=pk)
    return todo_list

def create_todo(name, todo_list):
    todo = ToDo(name=name, todo_list=todo_list)
    todo.save()
    return todo

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

    def test_post_todo(self):
        new_todo_list = create_todolist("Today's list")
        self.client = APIClient(enforce_csrf_checks=False)
        response = self.client.post(reverse('todos'), format='json', 
            data={'name': 'take out trash', 'todo_list_id': new_todo_list.pk}
        )
        self.assertEquals(response.json()['name'], "take out trash")

    def test_put_todo(self):
        new_todo_list = create_todolist("Today's list")
        todo_list = get_todo_list(pk=new_todo_list.pk)
        new_todo = create_todo("take out trash", new_todo_list)
        self.client = APIClient(enforce_csrf_checks=False)
        response = self.client.put(reverse('todos'), format='json',
            data={'todo_id': new_todo.pk, 'name': 'New Name!'}
        )
        self.assertEquals(response.json()['name'], "New Name!")