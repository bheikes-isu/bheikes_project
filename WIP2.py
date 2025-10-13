# %%
import openmeteo_requests as omr
import pandas as pd 
import requests_cache
from retry_requests import retry
from geopy.geocoders import Nominatim


def getcoordinates(userlocation):
    if (userlocation is None or userlocation==""):
        return ""
    geolocator=Nominatim(user_agent="Dress for the Weather")
    location=geolocator.geocode(userlocation)
    coordinates=[location.latitude, location.longitude]
    print(coordinates)
    return coordinates
 

def getweather():
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = omr.Client(session = retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "hourly": "temperature_2m", 
        "forecast_days": 1,
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "current": ["temperature_2m"],
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")
    #get rid of print statements

    # Process hourly data. The order of variables needs to be the same as requested.
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()

    #hourly_data = {"date": pd.Timestamp.today}

    #hourly_data["temperature_2m"] = hourly

    #hourly_dataframe = pd.DataFrame(data = hourly_data)
    print("\nHourly data\n", current_temperature_2m)

def weather (temperature):
    if temperature > 80:
        print("Shorts and a t-shirt")
    elif 60 <= temperature <= 70:
        print("Shorts and a t-shirt or a light jacket")
    elif 50 <= temperature < 60:
        print("pants and a longsleeve")
    elif 40 <= temperature < 50:
        print("pants and a longsleeve with a light jacket")


getcoordinates(None)


