import unittest
import joblib
import numpy as np
from app import app

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
        self.assertIn(b'Sugarcane Yield Predictor', response.data)  # Check if the content is as expected

    def test_prediction(self):
        # Test the prediction route with valid mock data
        raw_mock_data = {
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

        # Prepare raw data for scaling
        input_data = np.array([
            [
                raw_mock_data['wind_speed'],
                raw_mock_data['temp'],
                raw_mock_data['hum'],
                raw_mock_data['heat_idx'],
                raw_mock_data['pres'],
                raw_mock_data['prec'],
                raw_mock_data['co2_em_change'],
                raw_mock_data['co2_em_per_capita'],
                raw_mock_data['fossil_co2_em'],
                raw_mock_data['population'],
                raw_mock_data['pop_change']
            ]
        ])

        # Scale the input data
        scaled_data = self.scaler.transform(input_data)

        # Convert scaled data back to strings for form submission
        scaled_mock_data = {
            'wind_speed': str(scaled_data[0][0]),
            'temp': str(scaled_data[0][1]),
            'hum': str(scaled_data[0][2]),
            'heat_idx': str(scaled_data[0][3]),
            'pres': str(scaled_data[0][4]),
            'prec': str(scaled_data[0][5]),
            'co2_em_change': str(scaled_data[0][6]),
            'co2_em_per_capita': str(scaled_data[0][7]),
            'fossil_co2_em': str(scaled_data[0][8]),
            'population': str(scaled_data[0][9]),
            'pop_change': str(scaled_data[0][10])
        }

        # Send the scaled data to the /result endpoint
        response = self.app.post('/result', data=scaled_mock_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Predicted Sugarcane Yield:', response.data)  # Ensure the result page contains prediction text

if __name__ == '__main__':
    unittest.main()
