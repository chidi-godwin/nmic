from django import forms
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from . import forms, models
from .models import User


class RegisterView(View):
    template_name = 'users/signup.html'
    
    def get(self, request: HttpRequest):
        return render(request, self.template_name)
    
    def post(self, request: HttpRequest):
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.cleaned_data.pop('confirm_password')
            User.objects.create(**form.cleaned_data)
        return redirect('signup')