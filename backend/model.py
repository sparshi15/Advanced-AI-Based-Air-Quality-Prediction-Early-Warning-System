import pandas as pd
import numpy as np
from backend.database import conn
from tensorflow.keras.models import load_model

# load trained model
model = load_model("my_model.keras")

def get_latest_data():

    query = """
    SELECT pm25, pm10, no2, so2, co, o3, temperature
    FROM aqi_data
    ORDER BY created_at DESC
    LIMIT 24
    """

    df = pd.read_sql(query, conn)

    # reverse order so oldest → newest
    df = df[::-1]

    # handle case when less than 24 rows exist
    if len(df) < 24:
        missing = 24 - len(df)

        first_row = df.iloc[0]

        padding = pd.DataFrame([first_row] * missing)

        df = pd.concat([padding, df], ignore_index=True)

    return df


def predict_real_time_aqi():

    df = get_latest_data()

    data = df.values

    data = np.reshape(data, (1, 24, 7))

    prediction = model.predict(data)

    return float(prediction[0][0])
