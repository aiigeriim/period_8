from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms.project import ProjectForm
from webapp.models import Project, Task


class ProjectList(ListView):
    template_name = "project/main_page.html"
    context_object_name = "projects"
    model = Project
    ordering = '-created_at'


class ProjectDetail(DetailView):
    template_name = "project/project_detail.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = self.object.tasks.order_by('-created_at')
        return context


class ProjectCreate(CreateView):
    template_name = "project/create_project.html"
    form_class = ProjectForm


class ProjectUpdate(UpdateView):
    model = Project
    template_name = "project/update_project.html"
    form_class = ProjectForm


class ProjectDelete(DeleteView):
    template_name = "project/delete_project.html"
    model = Project
    success_url = reverse_lazy('webapp:project_list')




