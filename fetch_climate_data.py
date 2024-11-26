import requests
import pandas as pd
from datetime import datetime

# OpenWeather API URL
API_KEY = "your_api_key"
CITY = "London"
BASE_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&units=metric&cnt=5&appid={API_KEY}"

def fetch_climate_data():
    response = requests.get(BASE_URL)
    data = response.json()
    
    # Extract relevant data (Temperature, Humidity, etc.)
    climate_data = []
    for entry in data['list']:
        timestamp = datetime.utcfromtimestamp(entry['dt'])
        temperature = entry['main']['temp']
        humidity = entry['main']['humidity']
        weather = entry['weather'][0]['description']
        
        climate_data.append({
            'timestamp': timestamp,
            'temperature': temperature,
            'humidity': humidity,
            'weather': weather
        })
    
    return pd.DataFrame(climate_data)

climate_df = fetch_climate_data()
print(climate_df)
