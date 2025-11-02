from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from webapp.models import BaseCreateUpdateModel


class Project(BaseCreateUpdateModel):
    summary = models.CharField(max_length=100, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание проекта")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания", null=True, blank=True)
    participants = models.ManyToManyField(get_user_model(), verbose_name="Участник(и)",
                                          related_name="projects_part", blank=True)

    class Meta:
        db_table = "project"
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        permissions = [("add_participants", "Can add participants"), ("delete_participants", "Can delete participants")]

    def __str__(self):
        return self.summary

    def get_absolute_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.pk})
