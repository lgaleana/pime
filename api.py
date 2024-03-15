import requests
from dotenv import load_dotenv
import os

load_dotenv()

def search_flights(params):
    headers = {'apikey': os.getenv('TEQUILA_API_KEY')}
    response = requests.get('https://tequila-api.kiwi.com/v2/search', params=params, headers=headers)
    return response.json()
