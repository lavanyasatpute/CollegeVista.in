from django.shortcuts import render,HttpResponse,redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from Shiva.models import Contact
#import pandas as pd
#import joblib
#from django.http import FileResponse
from .tests import lavanya

def index(request):
    return render(request,'home.html')


def logout(request):
    return render(request,"signin.html")


def predict(request):
    if request.method == 'POST':
        Percentile = request.POST.get('Percentile')
        cast = request.POST.get('cast')
        pavan = lavanya(Percentile,cast)
        Context = {'pavan':pavan} 
        return render(request, 'FilterBranch.html', Context)

    

def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success_page')  # Redirect to a success page
    else:
        form = RegistrationForm()
    
    return render(request, 'Registration.html', {'form': form})
    

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful sign-in
        else:
            error_message = "Invalid username or password."
            return render(request, 'signin.html', {'error_message': error_message})
    else:
        return render(request, 'signin.html')


