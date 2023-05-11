from flask import Flask, request, jsonify, render_template

# Create the app object
app = Flask(__name__)


# importing function for calculations
from signe_function import basic_signe

# Define calculator
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    a = request.form['a']
    

    Resultat = basic_signe(a)

    return render_template('index.html', prediction_text=str(Resultat))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=82)

