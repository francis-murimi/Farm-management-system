from django import forms
from accounts.models import Ward,County
class WardForm(forms.Form):
    ward = forms.ModelChoiceField(
            queryset=Ward.objects.filter(county__name="Kirinyaga"))