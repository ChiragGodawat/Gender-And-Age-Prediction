from flask import Flask, render_template
import pickle
import pandas as pd

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # TODO: Load Data Set
    df = pd.read_csv('Test_Flask.csv')
    # TODO: Load Model
    model_age = pickle.load(open("Model_Age.sav", "rb"))
    model_gender = pickle.load((open("Model_Gender.sav", "rb")))
    # TODO: Make Predictions
    df_predict = pd.DataFrame()
    df_predict['Age_Group'] = model_age.predict(df)
    df_predict['Gender'] = model_gender.predict(df)

    dict = []

    age_mapping = {0: '0-24', 1: '25-32', 2: '32+'}
    gender_mapping = {0: 'Female', 1: 'Male'}

    # TODO: Iterate over rows of df
    for i in range(0, 50):
        device_id = i
        age = age_mapping[int(df_predict['Age_Group'][i])]
        gender = gender_mapping[int(df_predict['Gender'][i])]
        if (gender == "Female"):
            campaign = "Gender: Campaign 1 &2"
        else:
            campaign = "Gender: Campaign 3"

        if (age == '0-24'):
            campaign = campaign + "  Age: Campaign 4"
        elif (age == '25-32'):
            campaign = campaign + "  Age: Campaign 5"
        else:
            campaign = campaign + "  Age: Campaign 6"

        dict.append((device_id, age, gender, campaign))

    return render_template('results.html', results = dict)

if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0",port=8888)