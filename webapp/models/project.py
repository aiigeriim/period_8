from django.db import models
from django.urls import reverse

from webapp.models import BaseCreateUpdateModel


class Project(BaseCreateUpdateModel):
    summary = models.CharField(max_length=100, verbose_name="Название проекта",
                               null=True, blank=True)
    description = models.TextField(verbose_name="Описание проекта", null=True, blank=True)
    start_date = models.DateField(verbose_name="Дата начала", null=True, blank=True)
    end_date = models.DateField(verbose_name="Дата окончания", null=True, blank=True)

    class Meta:
        db_table = "project"
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.summary

    def get_absolute_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.pk})