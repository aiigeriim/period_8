from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import TaskForm
from webapp.models import Task


class TaskList(ListView):
    template_name = "task/main_page.html"
    context_object_name = "tasks"
    model = Task
    ordering = '-created_at'


class TaskDetail(DetailView):
    template_name = "task/task_detail.html"
    model = Task


class TaskCreate(CreateView):
    template_name = "task/create_task.html"
    form_class = TaskForm


class TaskUpdate(UpdateView):
    model = Task
    template_name = "task/update_task.html"
    form_class = TaskForm


class TaskDelete(DeleteView):
    template_name = "task/delete_task.html"
    model = Task
    success_url = reverse_lazy('webapp:main')


