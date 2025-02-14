from django import forms
from .models import Booking
from children.models import Child
from camp.models import Club

# Form for creating a new booking
# This form is used to create a new booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['club', 'child']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Get the logged-in user
        super().__init__(*args, **kwargs)
        # Filter child options to only show the parent's children
        self.fields['child'].queryset = Child.objects.filter(parent=user)