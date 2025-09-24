from django.forms.widgets import DateInput

from webapp.forms.base_form import BaseForm
from webapp.models import Project


class ProjectForm(BaseForm):

    class Meta:
        model = Project
        fields = ['summary', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'})
        }