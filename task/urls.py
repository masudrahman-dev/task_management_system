from django.urls import path

from .views import show_tasks, add_task
urlpatterns = [
    path('show_tasks/', show_tasks, name='show_tasks'),
    path('add_task/', add_task, name='add_task'),
    ]