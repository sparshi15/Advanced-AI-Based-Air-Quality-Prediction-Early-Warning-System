import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model
from backend.database import conn

model = load_model("aqi_lstm_model.h5")
scaler = joblib.load("scaler.pkl")

def predict_real_time_aqi():

    query = """
    SELECT pm25, pm10, no2, so2, co, o3, temperature
    FROM aqi_data
    ORDER BY created_at DESC
    LIMIT 24
    """

    df = pd.read_sql(query, conn)

    df = df[::-1]

    data = scaler.transform(df)

    data = np.reshape(data,(1,24,7))

    prediction = model.predict(data)

    return float(prediction[0][0])
