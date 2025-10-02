from django import forms
from webapp.forms.base_form import BaseForm
from webapp.models import Project


class ProjectParticipantsForm(BaseForm):

    class Meta:
        model = Project
        fields = ['participants']
        widgets = {
            'participants': forms.CheckboxSelectMultiple(),
        }