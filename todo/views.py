from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Task

# Create your views here.
def task_list(request):
    task = Task.objects.all().order_by('-Created_at')
    return render(request, 'todo/task_list.html', {'task':task})

def task_create(request):
    if request.method == 'POST':
        Title = request.POST.get('Title','').strip()      # ".strip()  this can remove the extra whitespace"
        Description = request.POST.get('Description','').strip()
        if Title:
            Task.objects.create(Title=Title, Description=Description)
            return redirect(reverse('todo:task_list'))
        error = "Title cannot be empty."
        return render(request, 'todo/task_create.html', {'error':error})
    return render(request, 'todo/task_create.html')

def task_update(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        Title = request.POST.get('Title','').strip()      # ".strip()  this can remove the extra whitespace"
        Description = request.POST.get('Description','').strip()
        Completed = request.POST.get('Completed') == 'on'
        if Title:
            task.Title = Title
            task.Description = Description
            task.Completed = Completed
            task.save()
            return redirect(reverse('todo:task_list'))
        else:
            return render(request, 'todo/task_create.html',{'task':task, 'error':"Title cannot be empty."})
    return render(request, 'todo/task_create.html',{'task':task})

def task_delete(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect(reverse('todo:task_list'))
    return render(request, 'todo/task_delete.html', {'task':task})

def task_toggle_complete(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.Completed = not task.Completed
        task.save()
    return redirect('todo:task_list')
    