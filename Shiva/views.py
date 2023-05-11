from django.shortcuts import render,HttpResponse,redirect
from Shiva.models import Contact
import pandas as pd
import joblib
from django.http import FileResponse

# Create your views here.
#reloadmodel = joblib.load('.\model\MINI-Project.pkl')

def index(request):
    return render(request,'home.html')


def about(request):
    return render(request,"index.html")

def getpredict(Percentile):
    classifer = joblib.load(open("trainModel.pkl",'rb')) 

    ram=joblib.load(open("trainModel2.pkl",'rb')) 

    #prediction(50)
    j=classifer.predict([[Percentile]])
    q = int(''.join(map(str, j-1)))
    result = ram.iloc[q:,0]
    return result


def predict(request):
    if request.method == 'POST':
        Percentile = request.POST.get('Percentile')
        result=getpredict(Percentile)
        # Process the imported data
        # You can perform any necessary operations on the imported data here
        
        return render(request, 'result.html', {'result'})
    
    return render(request, 'result.html')

def logout(request):
    return render(request,'logout.html')

