from django import forms
from django.forms import widgets
from webapp.models import Task


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for v in self.visible_fields():
            if not isinstance(v.field.widget, widgets.CheckboxSelectMultiple):
                v.field.widget.attrs['class'] = 'form-control'


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