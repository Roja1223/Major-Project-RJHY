import numpy as np
import joblib

def predict_pollution(option):
    tree_model = joblib.load('pollution_prediction.pkl')
    date = [float(option)]
    date = np.asarray(date, dtype=np.float32)
    date = date.reshape(-1, 1)
    print(date)
    temp = tree_model.predict(date)[0]
    print("-" * 2)
    print("\nThe pollution is estimated to be: " + str(temp) + "\n")
    print("-" * 2)
    return str(temp)