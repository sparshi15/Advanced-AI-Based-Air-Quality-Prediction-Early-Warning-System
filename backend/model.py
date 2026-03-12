import pandas as pd
import numpy as np
import joblib
from backend.database import conn
from tensorflow.keras.models import load_model

# load trained model
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

    # reverse order → oldest to newest
    df = df.iloc[::-1].reset_index(drop=True)

    # handle case when database has less than 24 rows
    if len(df) < 24:

        missing = 24 - len(df)

        if len(df) == 0:
            raise ValueError("No AQI data available in database")

        first_row = df.iloc[0]

        padding = pd.DataFrame([first_row] * missing, columns=df.columns)

        df = pd.concat([padding, df], ignore_index=True)

    return df


def predict_real_time_aqi():

    df = get_latest_data()

    # convert dataframe to numpy
    data = df.values

    # scale input
    data_scaled = scaler.transform(data)

    # reshape for LSTM
    data_scaled = np.reshape(data_scaled, (1, 24, 7))

    prediction_scaled = model.predict(data_scaled, verbose=0)

    # convert back to real AQI scale
    dummy = np.zeros((1, 7))
    dummy[0, -1] = prediction_scaled[0][0]

    prediction = scaler.inverse_transform(dummy)[0, -1]

    return float(prediction)
