from django.shortcuts import render,HttpResponse,redirect
from Shiva.models import Contact
#import pandas as pd
#import joblib
from django.http import FileResponse
from .tests import lavanya
#import pandas 
# Create your views here.
#classifer = joblib.load("TrainPKLmodel\trainModel.pkl")
#ram=joblib.load("TrainPKLmodel\trainModel2.pkl")

def index(request):
    return render(request,'home.html')


def about(request):
    return render(request,"index.html")



def predict(request):
    if request.method == 'POST':
        Percentile = request.POST.get('Percentile')
        #global result
        pavan = lavanya(Percentile)
        print('pavan:', pavan)
        Context = {'pavan':pavan}
        # Process the imported data
        # You can perform any necessary operations on the imported data here
        
        return render(request, 'result.html', Context)

    

def logout(request):
    return render(request,'logout.html')
