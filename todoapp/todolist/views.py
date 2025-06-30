# todolist/views.py
from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todolist/templates/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        TodoItem.objects.create(title=title)
    return redirect('todo_list')

def delete_todo(request, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return redirect('todo_list')
