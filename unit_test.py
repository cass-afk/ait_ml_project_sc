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
        self.assertIn(b'Sugar Cane Yield Prediction', response.data)  # Updated to match the title
  # Check if the content is as expected

    def test_prediction(self):
        # Test the prediction route with valid mock data
        mock_data = {
            'wind_speed': 5.0,
            'temp': 30.0,
            'hum': 60.0,
            'heat_idx': 32.0,
            'pres': 1013.0,
            'prec': 50.0,
            'co2_em_change': 1.2,
            'co2_em_per_capita': 4.5,
            'fossil_co2_em': 800.0,
            'population': 1000000,
            'pop_change': 2.1
        }
        scaler = joblib.load('scaler.pkl')
        mock_data = scaler.transform(pd.DataFrame([mock_data]))
        response = self.app.post('/result', data=mock_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Predicted Sugarcane Yield:', response.data)  # Ensure the result page contains prediction text

if __name__ == '__main__':
    unittest.main()
