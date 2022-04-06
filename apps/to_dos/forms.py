from django import forms

from to_dos.models import (
    Task,
)
class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = (
            'todo',
            'leadtime',
            'description'
        )
