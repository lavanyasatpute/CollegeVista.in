import joblib
import sys
import os
import pandas as pd 
import numpy as np 
from sklearn.tree import DecisionTreeClassifier


workpath = os.path.dirname(os.path.abspath(__file__))

# OBC cast model
data = pd.read_csv(os.path.join(workpath, "Cutoff_OBC.csv"))
model = DecisionTreeClassifier(random_state=42)
f =np.array(data["OBC"])
f = f.reshape(-1,1)
model.fit(f, data["Sr.No."])
joblib.dump(model, "OBCModel.pkl")
joblib.dump(data, "OBCModelData.pkl")

# Load model from file
#classifer = joblib.load("trainModel.pkl")


#prediction(50)
'''j=VJ.predict([[55]])
q = int(''.join(map(str, j-1)))
result = data2.iloc[q:,[1,2]]
print(result)'''

#ram=joblib.load("trainModel.pkl")

# VJ cast model
data2 = pd.read_csv(os.path.join(workpath, "VJ.csv"))
model2 = DecisionTreeClassifier(random_state=42)
f2 =np.array(data2["VJ"])
f2 = f2.reshape(-1,1)
model2.fit(f2, data2["Sr.No."])
joblib.dump(model2, "VJModel.pkl")
joblib.dump(data2, "VJModelData.pkl")

# Open cast madel
data3 = pd.read_csv(os.path.join(workpath, "Open.csv"))
model3 = DecisionTreeClassifier(random_state=42)
f3 =np.array(data3["Open"])
f3 = f3.reshape(-1,1)
model3.fit(f3, data3["Sr.No."])
joblib.dump(model3, "OpenModel.pkl")
joblib.dump(data3, "OpenModelData.pkl")

# ST cast model
data4 = pd.read_csv(os.path.join(workpath, "ST.csv"))
model4 = DecisionTreeClassifier(random_state=42)
f4 =np.array(data4["ST"])
f4 = f4.reshape(-1,1)
model4.fit(f4, data4["Sr.No."])
joblib.dump(model4, "STModel.pkl")
joblib.dump(data4, "STModelData.pkl")

# SC cast model
data5 = pd.read_csv(os.path.join(workpath, "SC .csv"))
model5 = DecisionTreeClassifier(random_state=42)
f5 =np.array(data5["SC"])
f5 = f5.reshape(-1,1)
model5.fit(f5, data5["Sr.No."])
joblib.dump(model5, "SCModel.pkl")
joblib.dump(data5, "SCModelData.pkl")

# SBC cast model
data6 = pd.read_csv(os.path.join(workpath, "SBC.csv"))
model6 = DecisionTreeClassifier(random_state=42)
f6 =np.array(data6["SBC"])
f6 = f6.reshape(-1,1)
model6.fit(f6, data6["Sr.No."])
joblib.dump(model6, "SBCModel.pkl")
joblib.dump(data6, "SBCModelData.pkl")

# NT-B cast model
data7 = pd.read_csv(os.path.join(workpath, "NT-B.csv"))
model7 = DecisionTreeClassifier(random_state=42)
f7 =np.array(data7["NT-B"])
f7 = f7.reshape(-1,1)
model7.fit(f7, data7["Sr.No."])
joblib.dump(model7, "NT-BModel.pkl")
joblib.dump(data7, "NT-BModelData.pkl")

# NT-C cast model
data8 = pd.read_csv(os.path.join(workpath, "NT-C.csv"))
model8 = DecisionTreeClassifier(random_state=42)
f8 =np.array(data8["NT-C"])
f8 = f8.reshape(-1,1)
model8.fit(f8, data8["Sr.No."])
joblib.dump(model8, "NT-CModel.pkl")
joblib.dump(data8, "NT-CModelData.pkl")

# NT-D cast model
data9 = pd.read_csv(os.path.join(workpath, "NT-D.csv"))
model9 = DecisionTreeClassifier(random_state=42)
f9 =np.array(data9["NT-D"])
f9 = f9.reshape(-1,1)
model9.fit(f9, data9["Sr.No."])
joblib.dump(model9, "NT-DModel.pkl")
joblib.dump(data9, "NT-DModelData.pkl")

