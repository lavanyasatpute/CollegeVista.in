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
import pymongo
from pymongo.server_api import ServerApi
#from urllib.parse import quote_plus


#import pandas as pd
#import joblib
#from django.http import FileResponse
from .tests import lavanya,generate_pdf,kit


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

def kit(request):
    return render(request,"kit.html")

def kitbranch(request):
    return render(request, 'KitHome.html')


def branch(request):
    if request.method == 'POST':
       Percentile = request.POST.get('Percentile')
       cast = request.POST.get('cast')
       pavan1 = kit(Percentile,cast)
       context = {'pavan1':pavan1}
       return render(request, 'Resultkit.html', context)
    
    
    
def pdf(request):
    if request.method == 'POST':
        #Percentile = request.POST.get('Percentile')
        #cast = request.POST.get('cast')
        #pavan = lavanya(Percentile,cast)
        L = generate_pdf(pavan)
        #L = generate_pdf(pavan1)
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
        pass2 = request.POST.get("pass1")

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        # Create the user
        uri = "mongodb+srv://collegevista:%40Lavanya2003@collegevista.dhtkzwn.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
        db = client["CollegeVista"]
        collection = db['myUser']
        dict = {'name':name,'username':username,'email':email,'password':pass1}
        collection.insert_one(dict)
        #Messages = "Your account was successfully created."

        return render(request, 'Signup.html')
        
        '''else:
            Messages2 = messages.success(request,"Your account was not successfully create.")

            return render(request, 'Signup.html',Messages2)'''

    return render(request, "Signup.html")  # Render the signup form template

    '''else:
            messages(request,"Your account is not Created , Please resister again .")

            return render(request,"Registration.html")'''
    
def signin(request):
    return render(request,"Signup.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        uri = "mongodb+srv://collegevista:%40Lavanya2003@collegevista.dhtkzwn.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
        db = client["CollegeVista"]
        collection = db['myUser']
        user = collection.find({'username':username})
       
        for item in user:
            
            if item['username']==username and item['password']==password:
               return render(request,'home.html')
            else:
                return HttpResponse("Sorry you are not user")
            
        '''if user['password']==password:
            return render(request, "home.html")

        else:
            error_message = "Invalid username or password."
            return render(request, 'Signup.html', {'error_message': error_message})'''
    else:
        return render(request, 'Signup.html')


