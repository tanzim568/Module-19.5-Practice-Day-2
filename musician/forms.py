from django import forms
from .models import Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model=Musician
        fields='__all__'
        
        labels = {
            'f_name':"First Name",
            'l_name':'Last Name',
        }
        widgets ={
            'phone_number':forms.TextInput(attrs={'type':'tel','placeholder':"Enter Mobile Number","class":'form-control',}),
            
        }