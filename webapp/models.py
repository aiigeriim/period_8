from django.db import models



class BaseCreateUpdateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True

class Task(BaseCreateUpdateModel):
    summary = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    status = models.ForeignKey("webapp.Status", on_delete=models.PROTECT, verbose_name="Статус", related_name="tasks")
    types = models.ManyToManyField("webapp.Type", verbose_name="Тип(ы)", related_name="task_set")

    class Meta:
        db_table = 'task'
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Status(BaseCreateUpdateModel):
    name = models.CharField(max_length=10, verbose_name="Статус", unique=True)

    class Meta:
        db_table = "status"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name


class Type(BaseCreateUpdateModel):
    name = models.CharField(max_length=10, verbose_name="Тип(ы)", unique=True)

    class Meta:
        db_table = "type"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.name



