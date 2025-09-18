from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import TaskForm
from webapp.models import Task

class TaskList(ListView):
    template_name = "task/main_page.html"
    context_object_name = "tasks"
    model = Task

    def get_queryset(self):
        return Task.objects.order_by('-created_at')


class TaskDetail(DetailView):
    template_name = "task/task_detail.html"

    def get_queryset(self):
        return Task.objects.all()


class TaskCreate(CreateView):
    template_name = "task/create_task.html"
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('webapp:detail', kwargs={'pk': self.object.pk})


class TaskUpdate(UpdateView):
    model = Task
    template_name = "task/update_task.html"
    form_class = TaskForm
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('webapp:detail', kwargs={'pk': self.object.pk})


class TaskDelete(DeleteView):
    template_name = "task/delete_task.html"
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('webapp:main')


