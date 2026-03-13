import pandas as pd
import numpy as np
import joblib
from backend.database import conn
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import os



# ---------- Rebuild model architecture ----------
model = Sequential()

model.add(LSTM(64, return_sequences=True, input_shape=(24, 7)))
model.add(Dropout(0.2))

model.add(LSTM(64))
model.add(Dropout(0.2))

model.add(Dense(1))

# Load trained weights
model.load_weights("delhi_lstm_weights.h5")

# Load scaler used during training
scaler = joblib.load("scaler.pkl")


# ---------- Fetch latest data from PostgreSQL ----------
def get_latest_data():
    query = """
    SELECT pm25, pm10, no2, so2, co, o3, aqi
    FROM aqi_data
    ORDER BY created_at DESC
    LIMIT 24
    """

    df = pd.read_sql(query, conn)

    # Reverse order (oldest → newest)
    df = df.iloc[::-1].reset_index(drop=True)

    # Handle case where DB has fewer than 24 rows
    if len(df) < 24:
        if len(df) == 0:
            raise ValueError("No AQI data found in database")

        missing = 24 - len(df)
        first_row = df.iloc[0]
        padding = pd.DataFrame([first_row] * missing, columns=df.columns)

        df = pd.concat([padding, df], ignore_index=True)

    return df


# ---------- Predict AQI ----------
def predict_real_time_aqi():

    df = get_latest_data()

    data = df.values

    # Scale using same scaler as training
    data_scaled = scaler.transform(data)

    # LSTM expects (batch, time_steps, features)
    data_scaled = np.reshape(data_scaled, (1, 24, 7))

    prediction_scaled = model.predict(data_scaled, verbose=0)

    # Convert prediction back to real AQI scale
    dummy = np.zeros((1, 7))
    dummy[0, -1] = prediction_scaled[0][0]

    prediction = scaler.inverse_transform(dummy)[0, -1]

    return float(prediction)
