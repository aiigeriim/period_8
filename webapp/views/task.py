from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import TaskForm
from webapp.models import Task, Project


class TaskDetail(DetailView):
    template_name = "task/task_detail.html"
    model = Task


class TaskCreate(CreateView, LoginRequiredMixin):
    template_name = "task/create_task.html"
    form_class = TaskForm

    def form_valid(self, form, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        form.instance.project = project
        return super().form_valid(form)


class TaskUpdate(UpdateView, LoginRequiredMixin):
    model = Task
    template_name = "task/update_task.html"
    form_class = TaskForm


class TaskDelete(DeleteView, LoginRequiredMixin):
    model = Task

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return self.object.get_absolute_url()


