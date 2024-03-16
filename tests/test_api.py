import unittest
from unittest.mock import patch
import api


class TestApi(unittest.TestCase):
    @patch('os.getenv')
    @patch('requests.get')
    def test_validate_city_name(self, mock_get, mock_getenv):
        mock_get.return_value.json.return_value = {'locations': []}
        mock_getenv.return_value = 'test_api_key'
        with self.assertRaises(ValueError):
            api.validate_city_name('invalid_city')

    @patch('os.getenv')
    @patch('requests.get')
    def test_search_flights(self, mock_get, mock_getenv):
        mock_get.return_value.json.return_value = {'flights': []}
        mock_getenv.return_value = 'test_api_key'
        result = api.search_flights({})
        self.assertEqual(result, {'flights': []})
