import requests
import os
from dotenv import load_dotenv

load_dotenv()

def validate_city_name(city_name: str):
    headers = {'apikey': os.getenv('TEQUILA_API_KEY')}
    params = {'term': city_name}
    response = requests.get('https://tequila-api.kiwi.com/locations/query', params=params, headers=headers)
    data = response.json()
    if not data['locations']:
        raise ValueError(f'Invalid city name: {city_name}')

def search_flights(params):
    headers = {'apikey': os.getenv('TEQUILA_API_KEY')}
    response = requests.get('https://tequila-api.kiwi.com/v2/search', params=params, headers=headers)
    return response.json()
