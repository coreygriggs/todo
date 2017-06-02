from django.shortcuts import render
from .models import ToDo, ToDoList
from .forms import AddToDoListForm

def index(request):
    if request.method == 'POST':
        form = AddToDoListForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            ToDoList.objects.create(name=name)
    todo_lists = ToDoList.objects.all()
    form = AddToDoListForm()
    return render(request, 'index.html', {'todo_lists': todo_lists, 'form': form})
