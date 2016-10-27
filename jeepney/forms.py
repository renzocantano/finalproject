from django import forms

from .models import Jeep

class jeepForm(forms.ModelForm):
    class Meta:
        model= Jeep
        fields = [
        "route",
        "place"
        ]
