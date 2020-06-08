from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime
from datetime import timedelta

from .models import Todo


def allTasks(request):
    tasks = Todo.objects.all().order_by('-created_date')
    all_tasks = []
    for task in tasks:
        t = {}
        t['id'] = task.id
        t['title'] = task.title
        t['message'] = task.message
        t['is_finished'] = task.is_finished
        t['in_progress'] = task.in_progress
        t['reopened'] = task.reopened
        t['created_date'] = task.created_date
        t['finish_date'] = task.finish_date
        t['due_date'] = task.due_date

        if task.due_date and (task.due_date < timezone.now()):
            days_passed = (f"{timezone.now() - task.due_date}").split('.')[0]
            t['passed_due'] = f"Task is passed due {days_passed}"
        all_tasks.append(t)

    return render(request, 'tasks/home.html', {'all_tasks': all_tasks})

def newTask(request):
    if request.method == "POST" and len(request.POST.get('to-do-text')) > 5:
        created_date = timezone.now()
        content = request.POST.get('to-do-text')
        message = request.POST.get('task-message')
        due_date = request.POST.get('date-picker')
        if due_date:
            due_date = datetime.strptime(due_date, "%Y-%m-%d")
            Todo.objects.create(
                title=content, 
                message=message, 
                created_date=created_date, 
                due_date=due_date)
        else:
            Todo.objects.create(title=content, message=message, created_date=created_date)

    return redirect('all_task')

def removeTask(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        task = Todo.objects.get(pk=task_id)
        if not task.is_finished or not task.in_progress:
            task.delete()
    return redirect('all_task')

def taskDetails(request):
    if request.method == "GET":
        task_id = request.GET.get('task_id')
        task = Todo.objects.get(pk=task_id)
        context = {
            'title' : task.title,
            'message': task.message,
            'is_finished': task.is_finished,
            'in_progress': task.in_progress,
            'created_date': task.created_date,
            'finish_date': task.finish_date
        }
        return JsonResponse(context)
    else:
        return redirect('all_task')
        
def updateTask(request):
    if request.method == "POST" and len(request.POST.get('title')) > 5:
        task_id = request.POST.get('task-id')
        title = request.POST.get('title')
        message = request.POST.get('task-message')
        stage = request.POST.get('stage')

        task = Todo.objects.get(pk=task_id)
        if task.is_finished:
            created_date = timezone.now()
            Todo.objects.create(title=title, message=message, created_date=created_date, reopened=True)
            return redirect('all_task')

        task.title = title
        task.message = message
        if stage == 'pending':
            task.is_finished = False
            task.in_progress = False
        elif stage == 'progress':
            task.in_progress = True
            task.is_finished = False
        elif stage == 'finished':
            task.in_progress = False
            task.is_finished = True
            task.finish_date = timezone.now()

        task.save()
        return redirect('all_task')