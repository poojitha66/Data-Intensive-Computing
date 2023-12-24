
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model_random_forest.pkl', 'rb'))


# Mapping for categorical features
cut_mapping = {'FAIR': 0, 'GOOD': 1, 'IDEAL': 2, 'PREMIUM': 3, 'VERY GOOD': 4}
color_mapping = {'D': 0, 'E': 1, 'F': 2, 'G': 3, 'H': 4, 'I': 5, 'J': 6}
clarity_mapping = {'I1': 0, 'IF': 1, 'SI1': 2, 'SI2': 3, 'VS1': 4, 'VS2': 5, 'VVS1': 6, 'VVS2': 7}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    cut = request.form.get('cut')
    color = request.form.get('color')
    clarity = request.form.get('clarity')
    carat = float(request.form.get('carat'))
    table = float(request.form.get('table'))
    x = float(request.form.get('x'))
    y = float(request.form.get('y'))
    z = float(request.form.get('z'))
    
    cut_mapped = cut_mapping[cut]
    color_mapped = color_mapping[color]
    clarity_mapped = clarity_mapping[clarity]
   

    input_features = np.array([[carat, cut_mapped, color_mapped, clarity_mapped,table, x, y, z]])

    prediction = model.predict(input_features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Diamond Price will be $ {}'.format(output))



if __name__ == "__main__":
    app.run(debug=True)