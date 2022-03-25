from django import forms
from .models import Farm
from django.contrib.auth.models import User

class FarmEditForm(forms.ModelForm):
    class Meta: 
        model = Farm
        fields = ['farm_size','water_availability','name']

class FarmAddForm(forms.ModelForm): 
    class Meta: 
        model = Farm 
        fields = ['county','ward','farm_size','water_availability','name']