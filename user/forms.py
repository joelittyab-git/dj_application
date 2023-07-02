from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import forms as defforms
from django.contrib. auth import authenticate
from django.contrib.auth.models import User 
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    UserChangeForm
)

        
class RegValidator():
        
    @staticmethod
    def validate_email(value):
        if(User.objects.filter(email=value).exists()):
            raise ValidationError(
                message='This email address has already been registered to this website',
            )
           

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        label='First Name:',
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"First Name",
                "aria-label":"First Name",
            }
        ),
        required=False,
        

    )
    
    last_name = forms.CharField(
        label='Last Name:',
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Last Name",
                "aria-label":"Username",
                "aria-describedby":"basic-addon1",
                
            }
        ),
        required=False
    )
    
    email = forms.EmailField(
        label='Email:',
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Email address*",
                "aria-label":"Email address",
                "aria-describedby":"basic-addon2",
            }    
        ),
        required=True,
        validators=[
            RegValidator.validate_email
        ]
    )
    
    username = forms.CharField(
        label='Username:',
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Username*",
                "aria-label":"Username",
                "aria-describedby":"basic-addon1",
                
            }   , 
        ),
        required=True
        
    )
    
    password1 = forms.CharField(
        label='Password:',
        widget=forms.PasswordInput(
            attrs={
                "type":"password",
                "class":"form-control",
                "id":"inputPassword1",
                "placeholder":"Password*",
            }
        ),
        required=True,
    )
    
    password2 =  forms.CharField(
        label='Password:',
        widget=forms.PasswordInput(
            attrs={
                "type":"password",
                "class":"form-control",
                "id":"inputPassword2",
                "placeholder":"Confirm Password*"
            }    
        ),
        required=True
    )
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            
        ]
            
    
    
class UserLoginForm(forms.Form):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "class": "form-control",
                "placeholder": "Username",
                "aria-label": "Username",
                "aria-describedby":"basic-addon1"
            }
        )
    )
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput( attrs={
                "autofocus": True,
                "class": "form-control",
                "placeholder": "Password",
                "aria-label": "Password",
                "aria-describedby":"basic-addon1"
            }),
    )

class UserAccountForm(defforms.UserChangeForm, forms.Form):
    
    profile_picture = forms.ImageField(
        
    )
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                "id":"staticEmail",
                "aria-describeby":"basic-addon1",   
                'readonly': True,
                'title': "You can't alter your username",
            }
        )
        
    )
    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'aria-describeby': "basic-addon2",
            }
        ),
        required=False,
    )
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
            }
        ),
        required=False,
    )
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
            }
        ),
        required=False,
    )
    
    class Meta:
        model = User
        exclude =  ['username','last_login', 'password', 'is_staff','is_active', 'is_superuser','user_permissions', 'groups']