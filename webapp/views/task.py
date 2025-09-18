from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView, ListView
from webapp.forms import TaskForm
from webapp.models import Task

class TaskList(ListView):
    template_name = "task/main_page.html"
    context_object_name = "tasks"
    model = Task

    def get_queryset(self):
        return Task.objects.order_by('-created_at')


class TaskDetail(TemplateView):
    template_name = "task/task_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = Task.objects.get(pk=self.kwargs["pk"])
        return context

class TaskCreate(FormView):
    template_name = "task/create_task.html"
    form_class = TaskForm
    model = Task

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:detail', kwargs={'pk': self.task.pk})


class TaskUpdate(FormView):
    template_name = "task/update_task.html"
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = Task.objects.get(pk=self.kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.task
        return kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:detail', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs["pk"]
        return get_object_or_404(Task, pk=pk)


class TaskDelete(View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        task.delete()
        return redirect("webapp:main")

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        return render(request, "task/delete_task.html", {"task":task})




