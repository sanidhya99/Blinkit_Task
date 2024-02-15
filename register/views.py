from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from .models import CustomUser
from .forms import RegistrationForm
from .manage import UserManager
class SignUpView(CreateView):
    model=CustomUser
    form_class=RegistrationForm
    success_url="/login"
    template_name="register/register.html"
        


