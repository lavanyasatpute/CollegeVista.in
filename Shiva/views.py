from django.shortcuts import render,HttpResponse,redirect
from Shiva.models import Contact
import pandas as pd
import joblib
# Create your views here.
reloadmodel = joblib.load('.\model\MINI-Project.pkl')

def index(request):
    return render(request,'home.html')


def about(request):
    return render(request,"index.html")

def predict(request):
    if request.method == "POST":
        Dict=[]
        Dict['category']=request.POST.get('Category')
        Dict2=[]
        Dict2['percentile']=request.POST.get('Percentile')

    score=reloadmodel.predict([Dict2])
    contex={'A':score}

    return render(request,"home.html",contex)

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')