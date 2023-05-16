from django.test import TestCase

import joblib

def lavanya(x, y):
    models = {
        "OBC": ("OBCModel.pkl", "OBCModelData.pkl"),
        "Open": ("OpenModel.pkl", "OpenModelData.pkl"),
        "VJ": ("VJModel.pkl", "VJModelData.pkl"),
        "SC": ("SCModel.pkl", "SCModelData.pkl"),
        "ST": ("STModel.pkl", "STModelData.pkl"),
        "SBC": ("SBCModel.pkl", "SBCModelData.pkl"),
        "NT-B": ("NT-BModel.pkl", "NT-BModelData.pkl"),
        "NT-C": ("NT-CModel.pkl", "NT-CModelData.pkl"),
        "NT-D": ("NT-DModel.pkl", "NT-DModelData.pkl")
    }
    
    if y in models:
        classifier = joblib.load(models[y][0])
        ram = joblib.load(models[y][1])
        
        j = classifier.predict([[x]])
        q = int(''.join(map(str, j - 1)))
        
        result = ram.iloc[q:, 2]
        percentile = ram.iloc[q:, 3]
        colleges = ram.iloc[q:, 1]
        
        colleges = list(colleges)
        result = list(result)
        percentile = list(percentile)

        my_list = []
        i = len(ram) - q
        
        for j in range(i - 1):
            my_dict = {}
            my_dict['colleges'] = colleges[j]
            my_dict['result'] = result[j]
            my_dict['percentile'] = percentile[j]
            my_list.append(my_dict)
        
        return my_list
    
    else:
        return 1

    