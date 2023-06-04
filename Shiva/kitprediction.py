import joblib

def kit1(x, y):
    models = {
        "OBC": ("KITOBCModel.pkl", "KITOBCModelData.pkl"),
        "Open": ("KITOpenModel.pkl", "KITOpenModelData.pkl"),
        "VJ": ("KITVJModel.pkl", "KITVJModelData.pkl"),
        "SC": ("KITSCModel.pkl", "KITSCModelData.pkl"),
        "ST": ("KITSTModel.pkl", "KITSTModelData.pkl"),
        "EWS": ("KITEWSModel.pkl", "KITEWSModelData.pkl"),
        "NT-B": ("KITNT-BModel.pkl", "KITNT-BModelData.pkl"),
        "NT-C": ("KITNT-CModel.pkl", "KITNT-CModelData.pkl"),
        "NT-D": ("KITNT-DModel.pkl", "KITNT-DModelData.pkl")
    }
    
    if y in models:
        classifier = joblib.load(models[y][0])
        ram = joblib.load(models[y][1])
        
        j = classifier.predict([[x]])
        q = int(''.join(map(str, j - 1)))
        
        Branches = ram.iloc[q:, 2].tolist()
        Percentile = ram.iloc[q:, 3].tolist()
        Colleges = ram.iloc[q:, 1].tolist()
        
        my_list = []
        i = len(ram) - q
        
        for j in range(i - 1):
            my_dict = {}
            my_dict['Colleges'] = Colleges[j]
            my_dict['Branches'] = Branches[j]
            my_dict['Percentile'] = Percentile[j]
            my_list.append(my_dict)
        
        return my_list
    
    else:
        return 1

def ladkit(x,y):
    models = {
        "OBC": ("Lad_KITOBCModel.pkl", "Lad_KITOBCModelData.pkl"),
        "Open": ("Lad_KITOpenModel.pkl", "Lad_KITOpenModelData.pkl"),
        "VJ": ("Lad_KITVJModel.pkl", "Lad_KITVJModelData.pkl"),
        "SC": ("Lad_KITSCModel.pkl", "Lad_KITSCModelData.pkl"),
        "ST": ("Lad_KITSTModel.pkl", "Lad_KITSTModelData.pkl"),
        "EWS": ("Lad_KITEWSModel.pkl", "Lad_KITEWSModelData.pkl"),
        "NT-B": ("Lad_KITNT-BModel.pkl", "Lad_KITNT-BModelData.pkl"),
        "NT-C": ("Lad_KITNT-CModel.pkl", "Lad_KITNT-CModelData.pkl"),
        "NT-D": ("Lad_KITNT-DModel.pkl", "Lad_KITNT-DModelData.pkl")
    }
    
    if y in models:
        classifier = joblib.load(models[y][0])
        ram = joblib.load(models[y][1])
        
        j = classifier.predict([[x]])
        q = int(''.join(map(str, j - 1)))
        
        Branches = ram.iloc[q:, 2].tolist()
        Percentile = ram.iloc[q:, 3].tolist()
        Colleges = ram.iloc[q:, 1].tolist()
        
        my_list = []
        i = len(ram) - q
        
        for j in range(i - 1):
            my_dict = {}
            my_dict['Colleges'] = Colleges[j]
            my_dict['Branches'] = Branches[j]
            my_dict['Percentile'] = Percentile[j]
            my_list.append(my_dict)
        
        return my_list
    
    else:
        return 1
    