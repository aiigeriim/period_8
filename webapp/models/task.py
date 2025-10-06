from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from webapp.models import BaseCreateUpdateModel


class Task(BaseCreateUpdateModel):
    summary = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание",
                                   blank=True, null=True)
    status = models.ForeignKey("webapp.Status", on_delete=models.PROTECT,
                               verbose_name="Статус", related_name="tasks")
    types = models.ManyToManyField("webapp.Type", verbose_name="Тип(ы)",
                                   related_name="task_set")
    project = models.ForeignKey("webapp.Project", related_name="tasks", on_delete=models.CASCADE, verbose_name="Проект")
    author = models.ForeignKey(get_user_model(), related_name='tasks', on_delete=models.SET_DEFAULT, default=1,
                               verbose_name="Автор")


    class Meta:
        db_table = 'task'
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


    def __str__(self):
        return self.summary

    def get_absolute_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.project_id})

