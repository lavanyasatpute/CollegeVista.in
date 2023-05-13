from django.test import TestCase

# Create your tests here.
import joblib
import pandas 

def lavanya(x):
    classifer = joblib.load("trainModel.pkl")

    ram=joblib.load("trainModel2.pkl")

    #prediction(50)
    j=classifer.predict([[x]])
    q = int(''.join(map(str, j-1)))
    result =(ram.iloc[q:,0])
    return result