from django.db import models
from webapp.models import BaseCreateUpdateModel


class Type(BaseCreateUpdateModel):
    name = models.CharField(max_length=10, verbose_name="Тип(ы)", unique=True)

    class Meta:
        db_table = "type"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.name