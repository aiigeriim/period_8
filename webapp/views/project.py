from urllib.parse import urlencode

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm, SearchForm
from webapp.forms.project import ProjectForm
from webapp.models import Project, Task


class ProjectList(ListView):
    template_name = "project/main_page.html"
    context_object_name = "projects"
    model = Project
    ordering = '-created_at'
    paginate_by = 5
    paginate_orphan = 1

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result["search_form"] = self.form
        if self.search_value:
            result['query'] = urlencode({'search': self.search_value})
            result['search'] = self.search_value
        return result

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']


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




