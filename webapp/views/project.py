from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms.project import ProjectForm
from webapp.models import Project


class ProjectList(ListView):
    template_name = "project/main_page.html"
    context_object_name = "projects"
    model = Project
    ordering = '-created_at'
#     template_name = "task/main_page.html"
#     context_object_name = "tasks"
#     model = Task
#     ordering = '-created_at'


class ProjectDetail(DetailView):
    template_name = "project/project_detail.html"
    model = Project

    # template_name = "task/task_detail.html"
    # model = Task


class ProjectCreate(CreateView):
    template_name = "project/create_project.html"
    form_class = ProjectForm



class ProjectUpdate(UpdateView):
    model = Project
    template_name = "project/update_project.html"
    form_class = ProjectForm


#     model = Task
#     template_name = "task/update_task.html"
#     form_class = TaskForm

#
class ProjectDelete(DeleteView):
    template_name = "project/delete_project.html"
    model = Project
    success_url = reverse_lazy('webapp:project_list')


#     template_name = "task/delete_task.html"
#     model = Task
#     success_url = reverse_lazy('webapp:main')


