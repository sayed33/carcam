from django import forms
from .models import CarCapture

class CarCaptureForm(forms.ModelForm):
    class Meta:
        model = CarCapture
        fields = ['image', 'car_type', 'car_number']
