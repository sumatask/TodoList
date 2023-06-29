from . models import Task
from django import  forms

class Todoform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }