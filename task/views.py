from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import TaskForm


def show_tasks(request):
    # tasks = TaskModel.objects.all()
    return render(request, 'task/show_tasks.html',)

def add_task(request):

    if request.method == 'POST':
        pass
        form = TaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            age = form.cleaned_data['age']
            print(age)

    else:
        form = TaskForm()
    return render(request, 'task/add_task.html',{'form':form})


