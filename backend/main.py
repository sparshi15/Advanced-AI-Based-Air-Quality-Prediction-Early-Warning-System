from fastapi import FastAPI
from fetch_api import get_air_quality
from database import conn, cursor
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()

# function to store data
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

    print("AQI data stored")

# API endpoint
@app.get("/")
def home():
    return {"message": "AQI Server Running"}

# manual trigger
@app.get("/store")
def store():
    store_data()
    return {"status": "data stored"}

# scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(store_data, "interval", hours=1)
scheduler.start()