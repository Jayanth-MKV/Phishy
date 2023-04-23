#importing required libraries

from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
import joblib
warnings.filterwarnings('ignore')
from feature import FeatureExtraction
from db.save_data import save_data


file = open("pickle/model.pkl","rb")
gbc = pickle.load(file)
file.close()
# gbc== joblib.load('joblib/gbc_model.joblib')


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        url = request.form["url"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30) 

        y_pred =gbc.predict(x)[0]
        #1 is safe       
        #-1 is unsafe
        # y_pro_phishing = gbc.predict_proba(x)[0,0]
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        return ({
            "url":url,
            "prob_not_phishy":round(y_pro_non_phishing,4)
        })
    return ({
        "url":""
    })


@app.route("/add_data", methods=["POST"])
def add_data():
    url = request.form["url"]
    label = request.form["label"]
    print(url,label)
    return save_data(url,label)

app.debug=True

if __name__ == "__main__":
    app.run()