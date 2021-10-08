from flask import Flask, render_template
import pickle
import pandas

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    #TODO: Load Data Set
    df = None
    #TODO: Load Model

    #TODO: Make Predictions

    #df['predictions'] = predictions

    dict = []

    #TODO: Iterate over rows of df
    for i in range(0,50):
        device_id = i
        age = i+20
        gender = "Male"
        campaign = "Campaign " + str(i)
        dict.append((device_id,age,gender,campaign))

    return render_template('results.html', results = dict)

if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0",port=8888)