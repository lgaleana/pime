import requests


def search_flights(params):
    response = requests.get('https://tequila-api.kiwi.com/v2/search', params=params)
    return response.json()
