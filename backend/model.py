import pandas as pd
import numpy as np
import joblib
from backend.database import conn
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# rebuild architecture
model = Sequential()

model.add(LSTM(64, return_sequences=True, input_shape=(24,7)))
model.add(Dropout(0.2))

model.add(LSTM(64))
model.add(Dropout(0.2))

model.add(Dense(1))

# load weights
model.load_weights("delhi_lstm_weights.h5")

# load scaler
scaler = joblib.load("scaler.pkl")
def predict_real_time_aqi():

    df = get_latest_data()

    data = df.values
    data_scaled = scaler.transform(data)

    data_scaled = np.reshape(data_scaled, (1,24,7))

    prediction_scaled = model.predict(data_scaled, verbose=0)

    dummy = np.zeros((1,7))
    dummy[0,-1] = prediction_scaled[0][0]

    prediction = scaler.inverse_transform(dummy)[0,-1]

    return float(prediction)
