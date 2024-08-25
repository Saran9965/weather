from django.forms import ModelForm,TextInput
from .models import city

class cityForm(ModelForm):
    class Meta:
        model=city
        fields=['Name']
        widgets={'Name':TextInput(attrs={'class':'form-control','placeholder':'city Name'})}