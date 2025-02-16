from django import forms
from .models import Child

class ChildForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'date_of_birth', 'emergency_contact']