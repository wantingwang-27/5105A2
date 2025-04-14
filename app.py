#### app.py ####

from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


app = Flask(__name__)

# Data from the table
data = {
    'Y_obs': [137, 118, 124, 124, 120, 129, 122, 142, 128, 114, 132, 130, 130, 112, 132, 117, 134, 132, 121, 128],
    'W': [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    'X': [19.8, 23.4, 27.7, 24.6, 21.5, 25.1, 22.4, 29.3, 20.8, 20.2, 27.3, 24.5, 22.9, 18.4, 24.2, 21.0, 25.9, 23.2, 21.6, 22.8]
}

df = pd.DataFrame(data)

# Fit linear regression
model = smf.ols('Y_obs ~ W + X', data=df).fit()

@app.route("/predict")
def predict():
    # Get both W and X parameters from the request
    w = float(request.args.get("W", 0))  # default to 0 if not provided
    x = float(request.args.get("X", 0))  # default to 0 if not provided
    
    # Create a DataFrame for prediction (must match the model's formula structure)
    new_data = pd.DataFrame({'W': [w], 'X': [x]})
    
    # Make prediction
    y_pred = model.predict(new_data)[0]
    
    # Log prediction
    with open("output.txt", "a") as f:  # changed to append mode
        f.write(f"Input W: {w}, X: {x}\nPrediction: {y_pred}\n\n")
    
    return jsonify({
        "input_W": w,
        "input_X": x,
        "prediction": y_pred
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
