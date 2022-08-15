import email
from django.shortcuts import render, redirect
from .form import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method =='POST':
        regis = SignupForm(request.POST)
        if regis.is_valid():
            user = regis.save()
            login(request, user)
            return redirect("login")
    else:
        regis = SignupForm()      
    return render(request, 'signup.html', {'regis': regis})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
            
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request, user)
            return redirect('signup')
    else:
        messages.error(request, '')
    return render(request, 'login.html')

