from django import forms
from .models import Album
from django.contrib.auth.forms import  UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields='__all__'
        
        widgets = {
            'release': forms.DateInput(attrs={'type':'date'}),
        }
        help_texts ={
            'name': "Write album name",
            'rating':'Choose a rating between 1 to 5'
        }
        
class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
        
class UserChangeForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')