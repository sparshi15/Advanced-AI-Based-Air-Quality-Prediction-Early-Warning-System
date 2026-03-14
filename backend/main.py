from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from backend.fetch_api import get_air_quality
from backend.database import conn, cursor
from backend.model import predict_real_time_aqi

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "AQI Server Running"}

# function to store AQI data
def store_data():

    data = get_air_quality()

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

    print("AQI data stored successfully")


# Manual route to store data
@app.post("/store")
def store():
    store_data()
    return {"status": "data stored successfully"}


# AQI prediction route
@app.get("/predict-aqi")
def predict_aqi():

    prediction = predict_real_time_aqi()

    return {
        "predicted_aqi": prediction
    }


# Scheduler
scheduler = BackgroundScheduler()

@app.on_event("startup")
def start_scheduler():

    scheduler.add_job(store_data, "interval", hours=1)
    scheduler.start()

    print("Scheduler started")



