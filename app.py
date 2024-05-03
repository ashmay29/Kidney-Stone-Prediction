import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]

    
    # pkl_file = open('scaler.pkl' , 'rb')
    # scaler = pickle.load(pkl_file)
    # final_features = scaler.fit_transform(final_features)

    prediction = model.predict(final_features)
    print(final_features)

    if prediction==1:
        return render_template('index.html', prediction_text='There exist very high chances that the patient has a kidney stone.')
    else:
        return render_template('index.html', prediction_text='The chances that the patient does has a kidney stone are very bleak.')    

if __name__ == "__main__":
    app.run(debug=True)