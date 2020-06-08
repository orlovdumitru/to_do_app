from django.urls import path
from . import views

name = 'tasks'

urlpatterns = [
    path('', views.allTasks, name='all_task'),
    path('newTask/', views.newTask, name='newTask'),
    path('taskDetails/', views.taskDetails, name='taskDetails'),
    path('removeTask/', views.removeTask, name='removeTask'),
    path('updateTask/', views.updateTask, name='updateTask'),
]
