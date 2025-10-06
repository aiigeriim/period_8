from urllib.parse import urlencode

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SearchForm, ProjectParticipantsForm, ProjectForm
from webapp.models import Project

User = get_user_model()

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
        context["tasks"] = self.object.tasks.order_by('-created_at').filter(is_deleted=False)
        return context


class ProjectCreate(LoginRequiredMixin, CreateView):
    template_name = "project/create_project.html"
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        form.instance.participants.add(self.request.user)
        return super().form_valid(form)


class ProjectAddParticipants(PermissionRequiredMixin, CreateView):
    template_name = "project/add_participant.html"
    form_class = ProjectParticipantsForm
    queryset = User.objects.all()
    model = Project

    permission_required = 'webapp.add_participants'


    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        participants = self.request.POST.getlist('participants')
        project.participants.set(participants)
        return HttpResponseRedirect(project.get_absolute_url())

    def has_permission(self):
        project = Project.objects.get(pk=self.kwargs['pk'])
        return super().has_permission() and self.request.user == project.author


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = "project/update_project.html"
    form_class = ProjectForm

    permission_required = 'webapp.change_project'

    def has_permission(self):
        project = Project.objects.get(pk=self.kwargs['pk'])
        return super().has_permission() and self.request.user == project.author


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    template_name = "project/delete_project.html"
    model = Project
    success_url = reverse_lazy('webapp:project_list')

    permission_required = 'webapp.delete_project'

    def has_permission(self):
        project = Project.objects.get(pk=self.kwargs['pk'])
        return super().has_permission() and self.request.user == project.author




