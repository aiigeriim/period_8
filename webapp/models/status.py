from django.db import models
from webapp.models import BaseCreateUpdateModel


class Status(BaseCreateUpdateModel):
    name = models.CharField(max_length=10, verbose_name="Статус", unique=True)

    class Meta:
        db_table = "status"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name