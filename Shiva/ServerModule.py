import sys
import os
import pandas as pd 
import numpy as np 
from sklearn.tree import DecisionTreeClassifier

def prediction(x):
    workpath = os.path.dirname(os.path.abspath(__file__))

    data = pd.read_csv(os.path.join(workpath, "Cutoff_OBC.csv"))
    model = DecisionTreeClassifier(random_state=42)
    #from sklearn.metrics import accuracy_score
    #accuracy_score(p,data["Sr.No."])

    f =np.array(data["OBC"])
    f = f.reshape(-1,1)
    model.fit(f, data["Sr.No."])
    #a=float(input("Enter the Persentile"))
    j= model.predict([[x]])
    q = int(''.join(map(str, j-1)))
    result = data.iloc[q:,0]
    return result

#prediction(50)
print(prediction(50))