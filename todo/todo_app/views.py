from django.shortcuts import render
from .models import ToDo, ToDoList, ListToDos
from .forms import AddToDoListForm, TodoForm

def index(request):
    if request.method == 'POST':
        form = AddToDoListForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            ToDoList.objects.create(name=name)
    todo_lists = ToDoList.objects.all()
    form = AddToDoListForm()
    return render(request, 'index.html', {'todo_lists': todo_lists, 'form': form})


def todo_list(request, pk):
    # attach new todo to todo list
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            todo = ToDo.objects.create(name=name, status='active')
            todo_list = ToDoList.objects.get(pk=pk)
            ListToDos.objects.create(todo_list=todo_list, todo=todo)              
    todo_list = ToDoList.objects.get(pk=pk) 
    todos = []
    if todo_list:
        list_to_dos = ListToDos.objects.filter(todo_list=todo_list)
        for item in list_to_dos:
            todos.append(item.todo)
    form = TodoForm()
    return render(request, 'todo.html', {'todos': todos, 'pk': pk, 'form': form})


def todo(request, pk):
    # complete task
    if request.method == 'PATCH':
        todo = ToDo.objects.get(pk=pk)
        if todo:
            todo.status = "complete"
            todo.save()