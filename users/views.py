from audioop import reverse
from re import template
from typing import Dict
from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from . import forms
from .models import User
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login


class Register(View):
    template_name = 'users/signup.html'
    
    def get(self, request: HttpRequest):
        
        if request.user.is_authenticated:
            return redirect('index')

        return render(request, self.template_name)
    
    def post(self, request: HttpRequest):
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.cleaned_data.pop('confirm_password')
            User.objects.create(**form.cleaned_data)
        return redirect('login')
    

class Login(View):
    template_name = 'users/sign-in.html'
    
    def get(self, request: HttpRequest):
        
        if request.user.is_authenticated:
            return redirect('index')

        return render(request, self.template_name)
    
    def post(self, request: HttpRequest):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data: Dict = form.cleaned_data
            user = authenticate(request, username=data.get('email'), password=data.get('password'))

            if user:
                login(request, user)
                
                return redirect('index')
            else:
                return render(request, self.template_name)
        return render(request, self.template_name)
            
          
class Index(TemplateView):
    template_name = 'users/info.html'