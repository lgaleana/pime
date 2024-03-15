import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from dotenv import load_dotenv
from main import app
import os

load_dotenv()

class TestMain(unittest.TestCase):

    @patch('main.api.search_flights', return_value={'flights': []})
    def test_search(self, mock_search_flights):
        client = TestClient(app)
        response = client.get('/search?from_city=city1&to_city=city2&date=2022-12-31')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'flights': []})
        mock_search_flights.assert_called_once_with({'from': 'city1', 'to': 'city2', 'date': '2022-12-31', 'apikey': os.getenv('TEQUILA_API_KEY')})
