from django import forms
from .models import MissionA, MissionP, Plant_Harvest, Animal_Harvest
from django.contrib.auth.models import User

class MissionPForm(forms.ModelForm):
    class Meta: 
        model = MissionP
        fields = ['crop','complete']


class MissionAForm(forms.ModelForm):
    class Meta: 
        model = MissionA
        fields = ['animal','complete']

class Plant_HarvestForm(forms.ModelForm): 
    class Meta: 
        model = Plant_Harvest
        fields = ['location','quantity','sold']

class Animal_HarvestForm(forms.ModelForm): 
    class Meta: 
        model = Animal_Harvest
        fields = ['location','quantity','sold']

