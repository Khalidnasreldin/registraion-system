from django.shortcuts import render, redirect

from . forms import RegisterForm
from django.contrib import messages

from . forms import LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request, 'app-t/index.html')

def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your account has been created successfully')
            return redirect('login')
    context = {'registerform':form}
    return render(request, 'app-t/register.html', context=context)

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'you have been logged in successfully')
                return redirect('dashboard')
    context={'loginform':form}
    return render(request, 'app-t/login.html', context=context)

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'app-t/dashboard.html')

def logout_view(request):
    auth.logout(request)
    return redirect('home')