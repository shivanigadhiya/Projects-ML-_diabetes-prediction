from flask import Flask,request,app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd
application = Flask(__name__)
app = application
scaler = pickle.load(open('Model\Standard1.pkl','rb'))
model = pickle.load(open('Model\modelforPrediction','rb'))
#Route
@app.route('/')
def index():
    return render_template('index.html')
#Route for single data point prediction

'''@app.route("/home")
def home():
    return render_template('home.html')'''
@app.route('/predictdata',methods = ["GET","POST"])
def predict_datapoint():
    result = ""
    
    if request.method == "POST":
        print("hello")
        Pregnancies = int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get("Glucose"))
        BloodPressure = float(request.form.get("BloodPressure"))
        SkinThickness = float(request.form.get("SkinThickness"))
        Insulin = float(request.form.get("Insulin"))
        BMI = float(request.form.get("BMI"))
        DiabetespedigreeFunction = float(request.form.get("DiabetesPedigreeFunction"))
        Age = float(request.form.get('Age'))
        new_data = scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetespedigreeFunction,Age]])

        predict = model.predict(new_data)
        if predict[0] == 1:
            result = 'Diabetic'
        else:
            result = 'Non-Diabetic'
        
        return render_template('single_prediction.html',result = result)
    else:
        return render_template('home.html')
if __name__ == "__main__":
    app.run(host = '0.0.0.0')


