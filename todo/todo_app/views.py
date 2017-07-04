from .models import ToDoList, ToDo
from rest_framework import viewsets, views, response
from .serializers import ToDoListSerializer, ToDoSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        self.data = data
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    def json(self):
        return self.data


class TodoListViewSet(views.APIView):

    def get(self, request, format='json'):
        todo_lists = ToDoList.objects.all()
        serializer = ToDoListSerializer(todo_lists, many=True)
        return JSONResponse(serializer.data, status=200)

    def post(self, request, format='json'):
        data = JSONParser().parse(request)
        if 'name' in data.keys():
            new_todo_list = ToDoList(name=data['name'])
            new_todo_list.save()
            return JSONResponse({
                'success': 'todo list created', 
                'name': new_todo_list.name,
                'todo_list_id': new_todo_list.pk
            }, status=201)
        else:
            return JSONResponse({'error': 'something went wrong'}, status=400)


class TodoViewSet(views.APIView):

    def get(self, request, format='json'):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return JSONResponse(serializer.data, status=200)

    def post(self, request, format='json'):
        data = JSONParser().parse(request)
        if 'todo_list_id' in data.keys():
            todo_list = ToDoList.objects.get(pk=data['todo_list_id'])
            todo = ToDo(name=data['name'], todo_list=todo_list)
            todo.save()
            return JSONResponse({
                'success': 'todo added to list',
                'name': data['name'],
                'todo_id': todo.pk
            })
        else:
            return JSONResponse({
                'error': 'something went wrong'
            }, status=400)
