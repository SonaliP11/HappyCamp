from django import forms
from .models import Child

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'date_of_birth', 'allergies', 'emergency_contact']