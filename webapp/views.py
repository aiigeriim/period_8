from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import TaskForm
from webapp.models import Task


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


class CreateTask(View):
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            summary = form.cleaned_data.get("summary")
            description = form.cleaned_data.get("description")
            status = form.cleaned_data.get("status")
            types = form.cleaned_data.get("types")
            task = Task.objects.create(
                summary=summary,
                description=description,
                status=status
            )
            task.types.set(types)
            return redirect("webapp:detail", pk=task.pk)
        else:
            return render(request,"create_task.html",{"form":form})

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request,"create_task.html",{"form":form})


class UpdateTask(View):
    def post(self, request, *args, pk, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data.get("summary")
            task.description = form.cleaned_data.get("description")
            task.status = form.cleaned_data.get("status")
            task.save()
            task.types.set(form.cleaned_data.get("types"))
            return redirect("webapp:detail", pk=task.pk)
        else:
            return render(request,"update_task.html",{"form":form, 'task':task})


    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        form = TaskForm(initial={
            "summary": task.summary,
            "description": task.description,
            "types": task.types.all(),
            "status": task.status,
        })
        return render(request,"update_task.html",{"form":form, 'task':task})


class DeleteTask(View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        task.delete()
        return redirect("webapp:main")

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        return render(request, "delete_task.html", {"task":task})




