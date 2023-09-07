from django.shortcuts import render, redirect
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib import messages
import os
from django.http import FileResponse
import pymongo
from pymongo.server_api import ServerApi
from .tests import lavanya, generate_pdf
from .kitprediction import GKIT_R1,LKIT_R1,LKIT_R2,GKIT_R2
import threading

def empty(request):
    return HttpResponse("Please Enter the Valid Url......")

def index(request):
    return render(request, 'home.html')

def logout(request):
    return render(request, "Signup.html")

def predict(request):
    if request.method == 'POST':
        Percentile = request.POST.get('Percentile')
        cast = request.POST.get('cast')
        number = request.POST.get('number')
        spec_branch = request.POST.get('spec_branch')
       # x = type(Percentile)
        if  not(Percentile and cast):
            return HttpResponse("Please Enter the Persentile and cast")

        t = threading.Thread(target=lavanya, args=(Percentile, cast))
        t.start()
        global pavan
        pavan = lavanya(Percentile, cast)
        t.join()
        number = int(number)
        if (len(pavan) <= number):
            pavan = [pavan[i] for i in range(len(pavan))]
        else:
            pavan = [pavan[i] for i in range(number)]
        if not(spec_branch):
            context = {'pavan': pavan}
            return render(request, 'FilterBranch.html', context)
        else:
            pavan = [pavan1 for pavan1 in pavan if pavan1['Branches'] == spec_branch]
            context = {'pavan': pavan}
            return render(request, 'FilterBranch.html', context)
          
    #else:
    #    return HttpResponse("Please create a account first !")

def kit(request):
    return render(request, "kit.html")

def kitbranch(request):
    return render(request, 'KitHome.html')

def branch(request):
    global pavan
    if request.method == 'POST':
        Percentile = request.POST.get('Percentile')
        cast = request.POST.get('cast')
        gender = request.POST.get('gender')
        Round = request.POST.get('Round')
        if Round == "Round1":
            if not(cast and Percentile and gender):
                return HttpResponse("Please Enter the Persentile and cast")
            else:
                if gender=='male':
                    t = threading.Thread(target=GKIT_R1, args=(Percentile, cast))
                    t.start()
                    pavan = GKIT_R1(Percentile, cast)
                    t.join()
                else:
                    t = threading.Thread(target=LKIT_R1, args=(Percentile, cast))
                    t.start()
                    pavan = LKIT_R1(Percentile, cast)
                    t.join()
        else:
            if not(cast and Percentile and gender):
                return HttpResponse("Please Enter the Persentile and cast")
            else:
                if gender=='male':
                    t = threading.Thread(target=GKIT_R2, args=(Percentile, cast))
                    t.start()
                    pavan = GKIT_R2(Percentile, cast)
                    t.join()
                else:
                    t = threading.Thread(target=LKIT_R2, args=(Percentile, cast))
                    t.start()
                    pavan = LKIT_R2(Percentile, cast)
                    t.join()
        context = {'pavan': pavan}
        return render(request,'ResultKit.html', context)


def filter(request):
    global filtered_pavan
    if request.method == 'POST':
        branchFilter = request.POST.get('branchFilter')
        #Cityfilter = request.POST.get('Cityfilter')
        if not(branchFilter):
            return HttpResponse("Please enter the Branch")
        else:
            filtered_pavan = [pavan1 for pavan1 in pavan if pavan1['Branches'] == branchFilter]
            context = {'filtered_pavan': filtered_pavan}
            return render(request, 'NewResult.html', context)

def filterpdf(request):
    if request.method == 'POST':
        t = threading.Thread(target=generate_pdf, args=(filtered_pavan,))
        t.start()
        L = generate_pdf(filtered_pavan)
        t.join()
        if os.path.exists(L):
            with open(L, 'rb') as file:
                response = HttpResponse(file, content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="College_Pdf.pdf"'
            return response
        else:
            return HttpResponse("PDF file not found.")


def pdf(request):
    if request.method == 'POST':
        t = threading.Thread(target=generate_pdf, args=(pavan,))
        t.start()
        L = generate_pdf(pavan)
        t.join()
        if os.path.exists(L):
            with open(L, 'rb') as file:
                response = HttpResponse(file, content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="College_Pdf.pdf"'
            return response
        else:
            return HttpResponse("PDF file not found.")

def Register(request):
    return render(request, "Registration.html")

def signup(request):
    if request.method == 'POST':
        #username = request.POST.get('username')
        #name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get("pass2")

        if pass1 != pass2:
            return HttpResponse("Passwords do not match")

        # Create the user
        uri = "mongodb+srv://collegevista:%40Lavanya2003@collegevista.dhtkzwn.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
        db = client["CollegeVista"]
        collection = db['myUser']
        data = {'id':1 ,'email': email, 'password': pass1}
        t = threading.Thread(target=collection.insert_one, args=(data,))
        t.start()
        collection.insert_one(data)

        return render(request, 'home.html')

def signin(request):
    return render(request, "home.html")

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        uri = "mongodb+srv://collegevista:%40Lavanya2003@collegevista.dhtkzwn.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
        db = client["CollegeVista"]
        collection = db['myUser']
        t = threading.Thread(target=collection.find, args=({'email': email},))
        t.start()
        user = collection.find({'email': email})
        for item in user:
            if item['email'] == email and item['password'] == password:
                #global token
                #token = collection.find({'id':id})
                #token['id']=1
                return render(request, 'home.html')

        return HttpResponse("Sorry, you are not a user")

    return render(request, 'home.html')

