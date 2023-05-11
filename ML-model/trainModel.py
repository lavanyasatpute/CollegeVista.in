import joblib
import sys
import os
import pandas as pd 
import numpy as np 
from sklearn.tree import DecisionTreeClassifier


workpath = os.path.dirname(os.path.abspath(__file__))

data = pd.read_csv(os.path.join(workpath, "Cutoff_OBC.csv"))
model = DecisionTreeClassifier(random_state=42)
#from sklearn.metrics import accuracy_score
#accuracy_score(p,data["Sr.No."])

f =np.array(data["OBC"])
f = f.reshape(-1,1)
model1=model.fit(f, data["Sr.No."])
#a=float(input("Enter the Persentile"))
#j= model.predict([[x]])
# Save model as pickle file
joblib.dump(model1, "trainModel.pkl")

# Load model from file
classifer = joblib.load("trainModel.pkl")


#prediction(50)
j=classifer.predict([[55]])
q = int(''.join(map(str, j-1)))
result = data.iloc[q:,0]
print(result)

joblib.dump(data, "trainModel2.pkl")
ram=joblib.load("trainModel.pkl")