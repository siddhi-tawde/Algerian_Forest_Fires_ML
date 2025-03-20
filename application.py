import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from flask import Flask , jsonify , render_template , request
import os 
application = Flask(__name__)
app = application

#import ridge regressor and standard scaler pickle
base_dir = os.path.dirname(os.path.abspath(__file__))
ridge_model = pickle.load(open(os.path.join(base_dir, 'models', 'ridge.pkl'), 'rb'))
standard_scalar = pickle.load(open(os.path.join(base_dir, 'models', 'scaler.pkl'), 'rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict_data",methods=['GET','POST'])
def predict_data():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled = np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        new_data_scaled = standard_scalar.transform(new_data_scaled)

        result=ridge_model.predict(new_data_scaled)
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')
def index():
    return render_template('index.html')

if __name__== "__main__":
    app.run(host="0.0.0.0",debug=True)