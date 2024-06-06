from django.forms import ModelForm,TextInput
from .models import kelvin

class ProjectForm(ModelForm):
    class Meta:
        model=kelvin
        fields=['title','image','description','demo_link','source_link','Tags']
        widgets = {
            'title': TextInput(attrs={
                'class':'project-title',
                'style':'color:brown'
            })
        }