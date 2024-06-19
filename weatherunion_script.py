import requests
from laggeddata import *

from datetime import datetime

now = datetime.now()

# Extract the current hour
current_hour = now.hour

API_KEY = "24b3227970223a36294433a167dc358b"
BASE_URL = "https://www.weatherunion.com/gw/weather/external/v0"

def get_locality_weather_data(locality_id):
    url = f"{BASE_URL}/get_locality_weather_data"
    headers = {
        "Content-Type": "application/json",
        "x-zomato-api-key": API_KEY
    }
    params = {
        "locality_id": locality_id
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data

kolkata='ZWL005429'
howrah='ZWL002488'
sectorV='ZWL002931'
airport='ZWL005435'
rabindrasadan='ZWL005244'
dakshindari='ZWL001499'

locality_weather_data = get_locality_weather_data(kolkata)

hourly_demand['temperature'] = locality_weather_data['locality_weather_data']['temperature']
hourly_demand['rain_intensity'] = locality_weather_data['locality_weather_data']['rain_intensity']
hourly_demand['rain_accumulation'] = locality_weather_data['locality_weather_data']['rain_accumulation']
hourly_demand['hour_of_day']=current_hour


locality_weather_data= get_locality_weather_data(rabindrasadan)
hourly_demand_rabindrasadan['temperature'] = locality_weather_data['locality_weather_data']['temperature']
hourly_demand_rabindrasadan['rain_intensity'] = locality_weather_data['locality_weather_data']['rain_intensity']
hourly_demand_rabindrasadan['rain_accumulation'] = locality_weather_data['locality_weather_data']['rain_accumulation']
hourly_demand_rabindrasadan['hour_of_day']=current_hour


locality_weather_data= get_locality_weather_data(dakshindari)
hourly_demand_dakshinDari['temperature'] = locality_weather_data['locality_weather_data']['temperature']
hourly_demand_dakshinDari['rain_intensity'] = locality_weather_data['locality_weather_data']['rain_intensity']
hourly_demand_dakshinDari['rain_accumulation'] = locality_weather_data['locality_weather_data']['rain_accumulation']
hourly_demand_dakshinDari['hour_of_day']=current_hour

locality_weather_data= get_locality_weather_data(airport)
hourly_demand_airpot['temperature'] = locality_weather_data['locality_weather_data']['temperature']
hourly_demand_airpot['rain_intensity'] = locality_weather_data['locality_weather_data']['rain_intensity']
hourly_demand_airpot['rain_accumulation'] = locality_weather_data['locality_weather_data']['rain_accumulation']
hourly_demand_airpot['hour_of_day']=current_hour

locality_weather_data= get_locality_weather_data(howrah)
hourly_demand_howrah['temperature'] = locality_weather_data['locality_weather_data']['temperature']
hourly_demand_howrah['rain_intensity'] = locality_weather_data['locality_weather_data']['rain_intensity']
hourly_demand_howrah['rain_accumulation'] = locality_weather_data['locality_weather_data']['rain_accumulation']
hourly_demand_howrah['hour_of_day']=current_hour

locality_weather_data= get_locality_weather_data(sectorV)
hourly_demand_sectorV['temperature'] = locality_weather_data['locality_weather_data']['temperature']
hourly_demand_sectorV['rain_intensity'] = locality_weather_data['locality_weather_data']['rain_intensity']
hourly_demand_sectorV['rain_accumulation'] = locality_weather_data['locality_weather_data']['rain_accumulation']
hourly_demand_sectorV['hour_of_day']=current_hour


hourly_demand=hourly_demand[['rain_intensity','rain_accumulation','temperature','hour_of_day','y_lag_1','y_lag_2','y_lag_10','y_lag_12','y_lag_14','y_lag_23','y_lag_24','y_lag_25']]
hourly_demand_airpot=hourly_demand_airpot[['rain_intensity','rain_accumulation','temperature','hour_of_day','y_lag_1','y_lag_2','y_lag_10','y_lag_12','y_lag_14','y_lag_23','y_lag_24','y_lag_25']]
hourly_demand_dakshinDari=hourly_demand_dakshinDari[['rain_intensity','rain_accumulation','temperature','hour_of_day','y_lag_1','y_lag_2','y_lag_10','y_lag_12','y_lag_14','y_lag_23','y_lag_24','y_lag_25']]
hourly_demand_howrah=hourly_demand_howrah[['rain_intensity','rain_accumulation','temperature','hour_of_day','y_lag_1','y_lag_2','y_lag_10','y_lag_12','y_lag_14','y_lag_23','y_lag_24','y_lag_25']]
hourly_demand_rabindrasadan=hourly_demand_rabindrasadan[['rain_intensity','rain_accumulation','temperature','hour_of_day','y_lag_1','y_lag_2','y_lag_10','y_lag_12','y_lag_14','y_lag_23','y_lag_24','y_lag_25']]
hourly_demand_sectorV=hourly_demand_sectorV[['rain_intensity','rain_accumulation','temperature','hour_of_day','y_lag_1','y_lag_2','y_lag_10','y_lag_12','y_lag_14','y_lag_23','y_lag_24','y_lag_25']]


print("city",hourly_demand)
print("dakshindari",hourly_demand_dakshinDari)
print("airpor",hourly_demand_airpot)
print('howrah',hourly_demand_howrah)
print('rabindrasadan',hourly_demand_rabindrasadan)
print('sector5',hourly_demand_sectorV)