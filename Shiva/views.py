from django.shortcuts import render,redirect
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .forms import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from Shiva.models import User
import os
from django.http import FileResponse
from pathlib import Path

#import pandas as pd
#import joblib
#from django.http import FileResponse
from .tests import lavanya,generate_pdf


def index(request):
    return render(request,'home.html')


def logout(request):
    return render(request,"Signup.html")


def predict(request):
    if request.method == 'POST':
        Percentile = request.POST.get('Percentile')
        cast = request.POST.get('cast')
        global pavan
        pavan = lavanya(Percentile,cast)
        Context = {'pavan':pavan} 
        return render(request, 'FilterBranch.html', Context)
    
def pdf(request):
    if request.method == 'POST':
        #Percentile = request.POST.get('Percentile')
        #cast = request.POST.get('cast')
        #pavan = lavanya(Percentile,cast)
        L = generate_pdf(pavan)
        if os.path.exists(L):
            # Open the PDF file
            with open(L, 'rb') as file:
                # Create a FileResponse with the PDF file
                response = HttpResponse(file, content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="College_Pdf.pdf"'

            # Return the FileResponse
            return response
        else:
            # Handle the case when the file doesn't exist
            return HttpResponse("PDF file not found.")
    

    

def Register(request):
    return render(request,"Registration.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get("pass2")

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        # Create the user
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = name
        myuser.save()

        messages.success(request, "Your account was successfully created.")
        return redirect("")

    return render(request, "signup.html")  # Render the signup form template

    '''else:
            messages(request,"Your account is not Created , Please resister again .")

            return render(request,"Registration.html")'''
    
def signin(request):
    return render(request,"Signup.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('info')  # Redirect to the home page after successful sign-in
        else:
            error_message = "Invalid username or password."
            return render(request, 'Signup.html', {'error_message': error_message})
    else:
        return render(request, 'Signup.html')


