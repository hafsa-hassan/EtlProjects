from dotenv import load_dotenv
import os
import requests # library for sending HTTP requests
import pyodbc # library to connect to ODBC - compliant databases such as microsoft sql server and azure sql
from datetime import datetime # datetime class from pythons built-in datetime module

# 1. Extract data
load_dotenv()

API_KEY = os.getenv("API_KEY")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")

url = "https://api.openweathermap.org/data/2.5/weather?"
cities = [
    "London", "New York", "Tokyo", "Paris", "Berlin", "Toronto",
    "Rio de Janeiro", "Mumbai", "Beijing", "Los Angeles", "Istanbul", "Dubai", "Dallas" ,"Atlanta"
]

# 3. Load data into Azure sql
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={DB_SERVER};'
    f'DATABASE={DB_NAME};'
    f'UID={DB_USER};'
    f'PWD={DB_PASSWORD}'
)

for city in cities:
    param = {
        "q": city,
        "appid": {API_KEY},
        "units": "metric",
    }

    response = requests.get(url, param).json()
    print(response)

    # 2. Transform data

    data = {
        "city": response["name"],
        "temp_celsius": response["main"]["temp"],
        "humidity": response["main"]["humidity"],
        "weather_description": response["weather"][0]["description"],
        "datetime": datetime.utcnow()
    }



    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO WeatherData(city, temp_celsius, humidity, weather_description, datetime)
        VALUES(?, ?, ?, ?, ?)
        """,
        data["city"], data["temp_celsius"], data["humidity"], data["weather_description"], data["datetime"]
    )
conn.commit()
conn.close()