from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task/show_tasks.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})
