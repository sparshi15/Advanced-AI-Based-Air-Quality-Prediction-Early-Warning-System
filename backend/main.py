from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from backend.fetch_api import get_air_quality
from backend.database import get_connection
from backend.model import predict_real_time_aqi

app = FastAPI()

# -------------------------
# Home Route
# -------------------------
@app.get("/")
def home():
    return {"message": "AQI Server Running"}


# -------------------------
# Store AQI Data
# -------------------------
def store_data():
    try:
        data = get_air_quality()

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO aqi_data
            (pm25, pm10, no2, so2, co, o3, temperature, humidity)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                data["pm25"],
                data["pm10"],
                data["no2"],
                data["so2"],
                data["co"],
                data["o3"],
                data["temperature"],
                data["humidity"]
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("AQI data stored successfully")

    except Exception as e:
        print("ERROR storing AQI data:", e)


# -------------------------
# Manual Store Route
# -------------------------
@app.get("/store")
def store():
    store_data()
    return {"status": "data stored successfully"}


# -------------------------
# Fetch Stored Data
# -------------------------
@app.get("/data")
def get_data():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM aqi_data ORDER BY created_at DESC LIMIT 10"
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"data": rows}


# -------------------------
# AQI Prediction
# -------------------------
@app.get("/predict-aqi")
def predict_aqi():

    prediction = predict_real_time_aqi()

    return {"predicted_aqi": prediction}


# -------------------------
# Scheduler
# -------------------------
scheduler = BackgroundScheduler()

@app.on_event("startup")
def start_scheduler():
    scheduler.add_job(store_data, "interval", hours=1)
    scheduler.start()

    print("Scheduler started")






