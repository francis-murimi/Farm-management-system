from django import forms
from .models import Farmer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class FarmerProfileForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['county','ward','national_id','phone_number','gender','disability'] 