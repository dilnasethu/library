from django import forms
from libraryapp.models import LibraryModel
from django.contrib.auth.models import User

class LibraryRegisterForm(forms.ModelForm):
    class Meta:
        model=LibraryModel
        fields=["first_name","last_name","username","password","place","role"]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            "username": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
            "password": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            "place": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            "role":forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
    
        }
        
       
class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]

class UserEditForm(forms.ModelForm):
    class Meta:
        model=LibraryModel
        fields=["first_name","last_name","username","password","place","role"]
    