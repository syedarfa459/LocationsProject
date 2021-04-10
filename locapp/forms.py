from django import forms
from .models import Destination, Tourist

class DestinationForm(forms.ModelForm):

    class Meta:
        model = Destination
        fields = ('destination',)

class TouristForm(forms.ModelForm):

    class Meta:
        model = Tourist
        fields = ('tourist_name','tourist_latitude','tourist_longitude','tourist_location')