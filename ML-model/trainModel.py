import joblib
import sys
import os
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

workpath = os.path.dirname(os.path.abspath(__file__))

# Define a function to train and save the model
def train_and_save_model(data_file, feature_column, target_column, model_file, data_file_dump):
    data = pd.read_csv(os.path.join(workpath, data_file))
    model = DecisionTreeClassifier(random_state=42)
    features = np.array(data[feature_column]).reshape(-1, 1)
    model.fit(features, data[target_column])
    joblib.dump(model, model_file)
    joblib.dump(data, data_file_dump)

# Train and save models for different caste categories
train_and_save_model("Cutoff_OBC.csv", "OBC", "Sr.No.", "OBCModel.pkl", "OBCModelData.pkl")
train_and_save_model("VJ.csv", "VJ", "Sr.No.", "VJModel.pkl", "VJModelData.pkl")
train_and_save_model("Open.csv", "Open", "Sr.No.", "OpenModel.pkl", "OpenModelData.pkl")
train_and_save_model("ST.csv", "ST", "Sr.No.", "STModel.pkl", "STModelData.pkl")
train_and_save_model("SC .csv", "SC", "Sr.No.", "SCModel.pkl", "SCModelData.pkl")
train_and_save_model("SBC.csv", "SBC", "Sr.No.", "SBCModel.pkl", "SBCModelData.pkl")
train_and_save_model("NT-B.csv", "NT-B", "Sr.No.", "NT-BModel.pkl", "NT-BModelData.pkl")
train_and_save_model("NT-C.csv", "NT-C", "Sr.No.", "NT-CModel.pkl", "NT-CModelData.pkl")
train_and_save_model("NT-D.csv", "NT-D", "Sr.No.", "NT-DModel.pkl", "NT-DModelData.pkl")
