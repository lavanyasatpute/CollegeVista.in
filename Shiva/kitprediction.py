import joblib

def GKIT_R1(x, y):
    models = {
        "OBC": ("GR1_OBC_Model.pkl", "GR1_OBC_Model_Data.pkl"),
        "OPEN": ("GR1_OPEN_Model.pkl", "GR1_OPEN_Model_Data.pkl"),
        "VJ": ("GR1_VJ_Model.pkl", "GR1_VJ_Model_Data.pkl"),
        "SC": ("GR1_SC_Model.pkl", "GR1_SC_Model_Data.pkl"),
        "ST": ("GR1_ST_Model.pkl", "GR1_ST_Model_Data.pkl"),
        "EWS": ("GR1_EWS_Model.pkl", "GR1_EWS_Model_Data.pkl"),
        "NT-B": ("GR1_NT-B_Model.pkl", "GR1_NT-B_Model_Data.pkl"),
        "NT-C": ("GR1_NT-C_Model.pkl", "GR1_NT-C_Model_Data.pkl"),
        "NT-D": ("GR1_NT-D_Model.pkl", "GR1_NT-D_Model_Data.pkl")
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

        for j in range(i):
            my_dict = {}
            my_dict['Colleges'] = Colleges[j]
            my_dict['Branches'] = Branches[j]
            my_dict['Percentile'] = Percentile[j]
            my_list.append(my_dict)

        return my_list

    else:
        z = [{'Colleges':"No colleges are found",'Branches':"No Branch Found",'Percentile':"00000000000000"}]
        return z

def LKIT_R1(x,y):

    models = {
        "OBC": ("LR1_OBC_Model.pkl", "LR1_OBC_Model_Data.pkl"),
        "OPEN": ("LR1_OPEN_Model.pkl", "LR1_OPEN_Model_Data.pkl"),
        "VJ": ("LR1_VJ_Model.pkl", "LR1_VJ_Model_Data.pkl"),
        "SC": ("LR1_SC_Model.pkl", "LR1_SC_Model_Data.pkl"),
        "ST": ("LR1_ST_Model.pkl", "LR1_ST_Model_Data.pkl"),
        "EWS": ("LR1_EWS_Model.pkl", "LR1_EWS_Model_Data.pkl"),
        "NT-B": ("LR1_NT-B_Model.pkl", "LR1_NT-B_Model_Data.pkl"),
        "NT-C": ("LR1_NT-C_Model.pkl", "LR1_NT-C_Model_Data.pkl"),
        "NT-D": ("LR1_NT-D_Model.pkl", "LR1_NT-D_Model_Data.pkl")
    }

    if y in models:
        classifier = joblib.load(models[y][0])
        ram = joblib.load(models[y][1])

        j = classifier.predict([[x]])
        q = int(''.join(map(str, j-1)))

        Branches = ram.iloc[q:, 2].tolist()
        Percentile = ram.iloc[q:, 3].tolist()
        Colleges = ram.iloc[q:, 1].tolist()

        my_list = []
        i = len(ram) - q

        for j in range(i):
            my_dict = {}
            my_dict['Colleges'] = Colleges[j]
            my_dict['Branches'] = Branches[j]
            my_dict['Percentile'] = Percentile[j]
            my_list.append(my_dict)

        return my_list

    else:
        z = [{'Colleges':"No colleges are found",'Branches':"No Branch Found",'Percentile':"00000000000000"}]
        return z

################################################################################################

def GKIT_R2(x, y):
    models = {
        "OBC": ("GR2_OBC_Model.pkl", "GR2_OBC_Model_Data.pkl"),
        "OPEN": ("GR2_OPEN_Model.pkl", "GR2_OPEN_Model_Data.pkl"),
        "VJ": ("GR2_VJ_Model.pkl", "GR2_VJ_Model_Data.pkl"),
        "SC": ("GR2_SC_Model.pkl", "GR2_SC_Model_Data.pkl"),
        "ST": ("GR2_ST_Model.pkl", "GR2_ST_Model_Data.pkl"),
        "EWS": ("GR2_EWS_Model.pkl", "GR2_EWS_Model_Data.pkl"),
        "NT-B": ("GR2_NT-B_Model.pkl", "GR2_NT-B_Model_Data.pkl"),
        "NT-C": ("GR2_NT-C_Model.pkl", "GR2_NT-C_Model_Data.pkl"),
        "NT-D": ("GR2_NT-D_Model.pkl", "GR2_NT-D_Model_Data.pkl")
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

        for j in range(i):
            my_dict = {}
            my_dict['Colleges'] = Colleges[j]
            my_dict['Branches'] = Branches[j]
            my_dict['Percentile'] = Percentile[j]
            my_list.append(my_dict)

        return my_list

    else:
        z = [{'Colleges':"No colleges are found",'Branches':"No Branch Found",'Percentile':"00000000000000"}]
        return z

def LKIT_R2(x,y):

    models = {
        "OBC": ("LR2_OBC_Model.pkl", "LR2_OBC_Model_Data.pkl"),
        "OPEN": ("LR2_OPEN_Model.pkl", "LR2_OPEN_Model_Data.pkl"),
        "VJ": ("LR2_VJ_Model.pkl", "LR2_VJ_Model_Data.pkl"),
        "SC": ("LR2_SC_Model.pkl", "LR2_SC_Model_Data.pkl"),
        "ST": ("LR2_ST_Model.pkl", "LR2_ST_Model_Data.pkl"),
        "EWS": ("LR2_EWS_Model.pkl", "LR2_EWS_Model_Data.pkl"),
        "NT-B": ("LR2_NT-B_Model.pkl", "LR2_NT-B_Model_Data.pkl"),
        "NT-C": ("LR2_NT-C_Model.pkl", "LR2_NT-C_Model_Data.pkl"),
        "NT-D": ("LR2_NT-D_Model.pkl", "LR2_NT-D_Model_Data.pkl")
    }

    if y in models:
        classifier = joblib.load(models[y][0])
        ram = joblib.load(models[y][1])

        j = classifier.predict([[x]])
        q = int(''.join(map(str, j-1)))

        Branches = ram.iloc[q:, 2].tolist()
        Percentile = ram.iloc[q:, 3].tolist()
        Colleges = ram.iloc[q:, 1].tolist()

        my_list = []
        i = len(ram) - q

        for j in range(i):
            my_dict = {}
            my_dict['Colleges'] = Colleges[j]
            my_dict['Branches'] = Branches[j]
            my_dict['Percentile'] = Percentile[j]
            my_list.append(my_dict)

        return my_list

    else:
        z = [{'Colleges':"No colleges are found",'Branches':"No Branch Found",'Percentile':"00000000000000"}]

        return z
