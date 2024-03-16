import requests
import os
from dotenv import load_dotenv

load_dotenv()

CITY_TO_KIWI_ID = {
'New York': 'NYC',
'Los Angeles': 'LAX',
'Chicago': 'CHI',
'Houston': 'HOU',
'Phoenix': 'PHX',
'Philadelphia': 'PHL',
'San Antonio': 'SAT',
'San Diego': 'SAN',
'Dallas': 'DFW',
'San Jose': 'SJC'
}

def search_flights(params):
    headers = {'apikey': os.getenv('TEQUILA_API_KEY')}
    params['fly_from'] = CITY_TO_KIWI_ID[params['fly_from']]
    response = requests.get('https://tequila-api.kiwi.com/v2/search', params=params, headers=headers)
    return response.json()
