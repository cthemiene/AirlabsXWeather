import requests
import json

# Set the API key
api_key = "APIKEY_HERE"

# Set the station ID
station_id = "GHCND:USW00014739"

# Make the request to the NOAA web service
# Instead of staion use either ATL lat and long or active flight lat and long
# https://api.weather.gov/points/{latitude},{longitude}
response = requests.get(f"https://www.ncdc.noaa.gov/cdo-web/api/v2/stations/{station_id}", headers={'token': api_key})

# Parse the JSON response
Weather_data = response.json()

# Print the response
print(Weather_data)
