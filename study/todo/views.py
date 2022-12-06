from django.shortcuts import render
from .forms import TodoForm
from django.http import HttpResponseRedirect


# Create your views here.
todos = []

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST) 
        if form.is_valid():
            todo_li = form.cleaned_data['todo_header']
            todos.append(todo_li)
            
    else:
        form = TodoForm()
    return render(request, 'todo/index.html', {'form': form})
    
def todo_list(request):
    return render(request, 'todo/todo_list.html', {
        "todos": todos
    })