from django.urls import path
from task import views

urlpatterns = [
    path('', views.show_tasks, name='show_tasks'),
    path('add_task/', views.add_task, name='add_task')
    ]