from django import forms
from django.forms import widgets

from webapp.models import Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(
    label='Название',
    required = True,
    widget = widgets.Input(attrs={"class": "form-control"}))
    description = forms.CharField(
    label='Описание',
    required = False,
    widget = widgets.Input(attrs={"class": "form-control"})
    )
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус', required=True, widget=forms.Select(attrs={"class": "form-control"}))
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Тип(ы)', required=True, widget=forms.Select(attrs={"class": "form-control"}))


class StatusForm(forms.Form):
    name = forms.CharField(
    label='Название',
    required = True,
    widget=widgets.Input(attrs={"class": "form-control"})
    )

class TypeForm(forms.Form):
    name = forms.CharField(
    label='Тип',
    required = True,
    widget=widgets.Input(attrs={"class": "form-control"})
    )