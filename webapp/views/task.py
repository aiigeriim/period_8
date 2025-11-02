from django.contrib.auth.mixins import  PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import TaskForm
from webapp.models import Task, Project


class TaskDetail(DetailView):
    template_name = "task/task_detail.html"
    model = Task


class TaskCreate(PermissionRequiredMixin, CreateView):
    template_name = "task/create_task.html"
    form_class = TaskForm

    permission_required = 'webapp.add_task'

    def form_valid(self, form, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        form.instance.project = project
        return super().form_valid(form)

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return super().has_permission() and self.request.user in project.participants.all()


class TaskUpdate(PermissionRequiredMixin, UpdateView):
    model = Task
    template_name = "task/update_task.html"
    form_class = TaskForm

    permission_required = 'webapp.change_task'

    def has_permission(self):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        return super().has_permission() and self.request.user in task.project.participants.all()


class TaskDelete(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = "task/delete_task.html"

    permission_required = 'webapp.delete_task'

    def has_permission(self):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        return super().has_permission() and self.request.user in task.project.participants.all()

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.object.get_absolute_url()






