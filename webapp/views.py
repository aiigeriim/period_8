from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from webapp.models import Task, Type, Status


# Create your views here.

class MainPage(TemplateView):
    template_name = "main_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        return context

class Detail(TemplateView):
    template_name = "task_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = Task.objects.get(pk=self.kwargs["pk"])
        return context

