from django import forms 
from .models import SiteModels,UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SiteForm(forms.ModelForm):
    
    class Meta:
        model = SiteModels
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description'}),
        }

class SignupForm(UserCreationForm):
    email=forms.EmailField(required=True)
    image=forms.ImageField(required=False)

    class Meta:
        model=User
        fields=['username','email','password1','password2','image']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email'] 

class ProfileImageForm(forms.ModelForm):
    remove_photo = forms.BooleanField(required=False)

    class Meta:
        model=UserProfile
        fields=['image']
