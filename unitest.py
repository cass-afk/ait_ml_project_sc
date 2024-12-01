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

        # Load the scaler
        self.scaler = joblib.load('scaler.pkl')  # Replace with your actual scaler path

    def test_home_page(self):
    # Test if the home page loads successfully
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sugarcane Yield Predictor', response.data)  # Updated to match the title
  # Check if the content is as expected


if __name__ == '__main__':
    unittest.main()
