from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import *
from .forms import *

def filter_test(request):
    users = User.objects.order_by('-created_at')
    my_filter = UserFilter(request.GET, queryset=users)
    users = my_filter.qs
    context = {'users':users,'filter_user':my_filter}
    return render(request, "index.html", context)

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'portfolio.html')

def user_login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')