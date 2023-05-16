from django.shortcuts import render,HttpResponse,redirect
#from Shiva.models import Contact
#import pandas as pd
#import joblib
#from django.http import FileResponse
from .tests import lavanya

def index(request):
    return render(request,'home.html')


def about(request):
    return render(request,"signup.html")


def predict(request):
    if request.method == 'POST':
        Percentile = request.POST.get('Percentile')
        cast = request.POST.get('cast')
        pavan = lavanya(Percentile,cast)
        Context = {'pavan':pavan} 
        return render(request, 'result.html', Context)

    

def Register(request):
    return render(request,'Registration.html')

def signin(request):
    return render(request, 'signin.html')
