import pandas as pd
import numpy as np
import joblib
from backend.database import conn
from tensorflow.keras.models import load_model

from tensorflow.keras.models import load_model

model = load_model("delhi_lstm_model.h5", compile=False)

# load scaler
scaler = joblib.load("scaler.pkl")


def get_latest_data():

    query = """
    SELECT pm25, pm10, no2, so2, co, o3, aqi
    FROM aqi_data
    ORDER BY created_at DESC
    LIMIT 24
    """

    df = pd.read_sql(query, conn)

    df = df[::-1]

    # padding if rows < 24
    if len(df) < 24:

        missing = 24 - len(df)

        first_row = df.iloc[0]

        padding = pd.DataFrame([first_row] * missing)

        df = pd.concat([padding, df], ignore_index=True)

    return df


def predict_real_time_aqi():

    df = get_latest_data()

    # scale input
    data_scaled = scaler.transform(df)

    data_scaled = np.reshape(data_scaled, (1, 24, 7))

    prediction_scaled = model.predict(data_scaled)

    # convert back to original AQI scale
    dummy = np.zeros((1,7))
    dummy[0,-1] = prediction_scaled

    prediction = scaler.inverse_transform(dummy)[0,-1]

    return float(prediction)
