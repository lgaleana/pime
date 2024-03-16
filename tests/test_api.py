import unittest
from unittest.mock import patch
import api

class TestApi(unittest.TestCase):
    @patch('os.getenv')
    @patch('requests.get')
    def test_search_flights(self, mock_get, mock_getenv):
        mock_get.return_value.json.return_value = {'flights': []}
        mock_getenv.return_value = 'test_api_key'
        result = api.search_flights({'fly_from': 'New York', 'to': 'Los Angeles', 'date': '2022-12-31'})
        self.assertEqual(result, {'flights': []})