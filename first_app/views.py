from django.shortcuts import render , redirect
from first_app.models import TaskModel
from first_app.forms import TaskForm
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
# Create your views here.
class task_form(CreateView) :
    model = TaskModel
    template_name = 'task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('show_task')
    
def show_task(request) : 
    tasks = TaskModel.objects.all()
    return render(request , 'show_task.html' , {'tasks':tasks})

class delete_task(DeleteView) : 
    model = TaskModel
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('show_task')

class edit_task(UpdateView) : 
    model = TaskModel
    template_name = 'edit_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('show_task')
    
def mark_completed(request , id) :
    task = TaskModel.objects.get(id = id)
    task.is_completed = True
    task.save()
    return redirect('completed')
    
def completed(request) : 
    task = TaskModel.objects.all()
    return render(request ,'completed.html' , {'completed_tasks':task})