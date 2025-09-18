from django.db import models
from webapp.models import BaseCreateUpdateModel


class Task(BaseCreateUpdateModel):
    summary = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание",
                                   blank=True, null=True)
    status = models.ForeignKey("webapp.Status", on_delete=models.PROTECT,
                               verbose_name="Статус", related_name="tasks")
    types = models.ManyToManyField("webapp.Type", verbose_name="Тип(ы)",
                                   related_name="task_set")

    class Meta:
        db_table = 'task'
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.summary