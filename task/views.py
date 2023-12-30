from django.shortcuts import render, redirect
from .forms import TaskForm


def show_tasks(request):
    # tasks = TaskModel.objects.all()
    return render(request, 'task/show_tasks.html',)

def add_task(request):
    print(request)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')

    else:
        form = TaskForm()
    return render(request,'task/add_task.html')