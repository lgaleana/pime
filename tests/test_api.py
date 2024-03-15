import unittest
from unittest.mock import patch
from dotenv import load_dotenv
import api
import os

load_dotenv()

class TestApi(unittest.TestCase):
    @patch('requests.get')
    def test_search_flights(self, mock_get):
        mock_get.return_value.json.return_value = {'flights': []}
        result = api.search_flights({'apikey': os.getenv('TEQUILA_API_KEY')})
        self.assertEqual(result, {'flights': []})
