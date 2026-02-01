from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

class Register(View):
    def get(self, request):
        form = forms.RegisterForm()

        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = forms.RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.email = form.cleaned_data["email"]
            user.save()

            return redirect('login')
        return render(request, 'register.html', {'form': form}) 

class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("")
        
        return redirect("register")