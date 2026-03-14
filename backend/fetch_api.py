import requests
import os

API_KEY = os.getenv("OPENWEATHER_KEY")

def get_air_quality():

    if not API_KEY:
        raise Exception("OPENWEATHER_KEY not found in environment variables")

    lat = 28.6139
    lon = 77.2090

    air_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    try:

        air_response = requests.get(air_url, timeout=10)
        weather_response = requests.get(weather_url, timeout=10)

        air_data = air_response.json()
        weather_data = weather_response.json()

        comp = air_data["list"][0]["components"]

        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]

        return {
            "pm25": comp["pm2_5"],
            "pm10": comp["pm10"],
            "no2": comp["no2"],
            "so2": comp["so2"],
            "co": comp["co"],
            "o3": comp["o3"],
            "temperature": temperature,
            "humidity": humidity
        }

    except Exception as e:

        print("API ERROR:", e)

        return {
            "pm25": 0,
            "pm10": 0,
            "no2": 0,
            "so2": 0,
            "co": 0,
            "o3": 0,
            "temperature": 0,
            "humidity": 0
        }
