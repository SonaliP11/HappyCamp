from django import forms
from .models import Booking
from children.models import Child
from camp.models import Club

class BookingForm(forms.ModelForm):
    club = forms.ModelChoiceField(
        queryset=Club.objects.all(),
        required=True,
        empty_label="Please select activity from club",
        widget=forms.Select()
    )
    child = forms.ModelChoiceField(
        queryset=Child.objects.all(),
        required=True,
        empty_label="Please select your child name",
        widget=forms.Select()
    )

    class Meta:
        model = Booking
        fields = ['club', 'child']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Get the logged-in user
        super().__init__(*args, **kwargs)
        # Filter child options to only show the parent's children
        self.fields['child'].queryset = Child.objects.filter(parent=user)