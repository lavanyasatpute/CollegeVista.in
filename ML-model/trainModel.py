import joblib
import os
import pandas as pd 
import numpy as np 
from sklearn.tree import DecisionTreeClassifier

workpath = os.path.dirname(os.path.abspath(__file__))

cast_models = {
    "OBC": "Cutoff_OBC.csv",
    "VJ": "VJ.csv",
    "OPEN": "Open.csv",
    "ST": "ST.csv",
    "SC": "SC .csv",
    "SBC": "SBC.csv",
    "NT-B": "NT-B.csv",
    "NT-C": "NT-C.csv",
    "NT-D": "NT-D.csv"
}

for cast, filename in cast_models.items():
    data = pd.read_csv(os.path.join(workpath, filename))
    model = DecisionTreeClassifier(random_state=42)
    feature = np.array(data[cast]).reshape(-1, 1)
    model.fit(feature, data["Sr.No."])
    joblib.dump(model, f"{cast}Model.pkl")
    joblib.dump(data, f"{cast}ModelData.pkl")
