import unittest
from fastapi.testclient import TestClient
from main import app

class TestStatic(unittest.TestCase):

    def test_css_files(self):
        client = TestClient(app)
        response = client.get('/static/css/search.css')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/css', response.headers['content-type'])
        response = client.get('/static/css/results.css')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/css', response.headers['content-type'])
