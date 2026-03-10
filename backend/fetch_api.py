import requests

API_KEY = "aab3e602450dcc93b24ffbade158809f"
def get_air_quality():

    lat = 28.6139
    lon = 77.2090

    air_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    air_data = requests.get(air_url).json()
    weather_data = requests.get(weather_url).json()

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