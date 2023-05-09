from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    return render(request, 'meet_balls_app/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request,'meet_balls_app/home.html', {'user': {'is_authenticated': True}})
        else:   
            error_message = "Invalid username or password."
            messages.error(request, error_message)
            return render(request, 'meet_balls_app/login.html')
    else:
        return render(request, 'meet_balls_app/login.html')

def logout(request):
    return render(request, 'meet_balls_app/home.html', {'user': {'is_authenticated': False}})

def register(request):
    return render(request, 'meet_balls_app/home.html')
