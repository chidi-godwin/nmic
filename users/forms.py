from typing import Any, Dict
from django import forms
from django.core.validators import MinLengthValidator
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm, ValidationError
from .models import User
from django.utils.translation import gettext_lazy as _


class RegistrationForm(ModelForm):
    confirm_password = forms.CharField(label=_('confirm_password'), max_length=200)
    
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password']
        
    def clean(self) -> Dict[str, Any]:
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if len(password) < 8:
            raise ValidationError(
                _('password should contain at least 8 characters'),
                code='invalid'
            )
        
        if password != confirm_password:
            raise ValidationError(
                _('password doesn\'t match'),
                code='invalid'
            )
            
        cleaned_data['password'] = make_password(cleaned_data.get('password'))
        return cleaned_data
    

class LoginForm(forms.Form):
    email = forms.EmailField(label=_('confirm_password'), max_length=200)
    password = forms.CharField(max_length=200, validators=[MinLengthValidator(8)])
