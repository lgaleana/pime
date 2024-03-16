import unittest
from fastapi.testclient import TestClient
from main import app

# Existing tests...

# New tests for responsive design

# Test for results page

class TestResponsiveResults(unittest.TestCase):

    def test_responsive_design(self):
        client = TestClient(app)
        response = client.get('/static/css/results.css')
        self.assertEqual(response.status_code, 200)
        self.assertIn('@media', response.text)

# Test for search page

class TestResponsiveSearch(unittest.TestCase):

    def test_responsive_design(self):
        client = TestClient(app)
        response = client.get('/static/css/search.css')
        self.assertEqual(response.status_code, 200)
        self.assertIn('@media', response.text)