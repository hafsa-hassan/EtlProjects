# Weather Data ETL to Azure SQL

This Python script extracts current weather data for multiple cities from the OpenWeatherMap API, transforms the data into a simplified format, and loads it into an Azure SQL database table. It demonstrates a basic ETL (Extract, Transform, Load) pipeline.

---

## Features

- Fetches weather data (temperature, humidity, description) for a list of cities
- Uses environment variables to securely manage API keys and database credentials
- Connects to Azure SQL Database via `pyodbc`
- Inserts data with timestamps for historical tracking

---

## Prerequisites

- Python 3.7+
- `requests` library
- `pyodbc` library
- `python-dotenv` library
- ODBC Driver 17 for SQL Server installed on your machine
- Access to an Azure SQL Database with a table named `WeatherData`:

```sql
CREATE TABLE WeatherData (
    city VARCHAR(100),
    temp_celsius FLOAT,
    humidity INT,
    weather_description VARCHAR(255),
    datetime DATETIME
);
