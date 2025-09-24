from django import forms
from webapp.forms.base_form import BaseForm
from webapp.models import Task


class TaskForm(BaseForm):

    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'types']
        widgets = {
            'types': forms.CheckboxSelectMultiple(),
        }

    def clean_description(self):
        description = self.cleaned_data['description']
        if description == '':
            raise forms.ValidationError('Введите подробности задачи')
        return description

    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if len(summary) < 3:
            raise forms.ValidationError('Введите полное название задачи')
        return summary

