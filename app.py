from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load(open('final_best_model_sugarcane_yield.pkl', 'rb'))
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predictor')
def predictor():
    return render_template('predictor.html')

@app.route('/result', methods=['POST'])
def result():
    # Collect features from the form input
    wind_speed = float(request.form.get('wind_speed'))
    temp = float(request.form.get('temp'))
    hum = float(request.form.get('hum'))
    heat_idx = float(request.form.get('heat_idx'))
    pres = float(request.form.get('pres'))
    prec = float(request.form.get('prec'))
    co2_em_change = float(request.form.get('co2_em_change'))
    co2_em_per_capita = float(request.form.get('co2_em_per_capita'))
    fossil_co2_em = float(request.form.get('fossil_co2_em'))
    population = float(request.form.get('population'))
    pop_change = float(request.form.get('pop_change'))


    # Create a DataFrame for prediction
    input_data = pd.DataFrame([[wind_speed, temp, hum, heat_idx, pres, prec, fossil_co2_em, co2_em_change, co2_em_per_capita, population, pop_change ]], 
                              columns=['wind_speed', 'temp', 'hum', 'heat_idx', 'pres', 'prec','fossil_co2_em','co2_em_change', 'co2_em_per_capita',  'population', 'pop_change'])
    # Predict yield using the model
    predicted_yield = model.predict(input_data)[0]

    # Pass the prediction to the template
    return render_template('result.html', predicted_yield=predicted_yield)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
