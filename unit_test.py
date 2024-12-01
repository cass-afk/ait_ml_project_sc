import unittest
import joblib
import numpy as np
from app import app
import pandas as pd

class TestApp(unittest.TestCase):

    def setUp(self):
        # Create a test client for the Flask application
        self.app = app.test_client()
        self.app.testing = True


    def test_home_page(self):
        # Test if the home page loads successfully
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Update to match the actual title

if __name__ == '__main__':
    unittest.main()
