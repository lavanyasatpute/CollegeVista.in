from django.test import TestCase

# Create your tests here.
import joblib
import pandas 

def lavanya(x,y):
    if y=="OBC":
        classifer = joblib.load("OBCModel.pkl")
        ram=joblib.load("OBCModelData.pkl")
        j=classifer.predict([[x]])
        q = int(''.join(map(str, j-1)))
        result =(ram.iloc[q:,0])
        return result
    
    elif y=="Open":
        classifer = joblib.load("OpenModel.pkl")
        ram=joblib.load("OpenModelData.pkl")
        j=classifer.predict([[x]])
        q = int(''.join(map(str, j-1)))
        result =(ram.iloc[q:,1])
        return result
    
    elif y=="VJ":
        classifer = joblib.load("VJModel.pkl")
        ram=joblib.load("VJModelData.pkl")
        j=classifer.predict([[x]])
        q = int(''.join(map(str, j-1)))
        result =(ram.iloc[q:,1])
        return result
    
    elif y=="SC":
        classifer = joblib.load("SCModel.pkl")
        ram=joblib.load("SCModelData.pkl")
        j=classifer.predict([[x]])
        q = int(''.join(map(str, j-1)))
        result =(ram.iloc[q:,1])
        return result
    
    elif y=="ST":
        classifer = joblib.load("STModel.pkl")
        ram=joblib.load("STModelData.pkl")
        j=classifer.predict([[x]])
        q = int(''.join(map(str, j-1)))
        result =(ram.iloc[q:,1])
        return result
    
    elif y=="SBC":
        classifer = joblib.load("SBCModel.pkl")
        ram=joblib.load("SBCModelData.pkl")
        j=classifer.predict([[x]])
        q = int(''.join(map(str, j-1)))
        result =(ram.iloc[q:,1])
        return result
    
    elif y=="NT-B":
        classifer = joblib.load("NT-BModel.pkl")
        ram=joblib.load("NT-BModelData.pkl")
        j=classifer.predict([[x]])
        q = int(''.join(map(str, j-1)))
        result =(ram.iloc[q:,1])
        return result
    
    elif y=="NT-C":
        classifer = joblib.load("NT-CModel.pkl")
        ram=joblib.load("NT-CModelData.pkl")
        j=classifer.predict([[x]])
        q = int(''.join(map(str, j-1)))
        result =(ram.iloc[q:,1])
        return result
    
    elif y=="NT-D":
        classifer = joblib.load("NT-DModel.pkl")
        ram=joblib.load("NT-DModelData.pkl")
        j=classifer.predict([[x]])
        q = int(''.join(map(str, j-1)))
        result =(ram.iloc[q:,1])
        return result
    
    else:
        return 1
    