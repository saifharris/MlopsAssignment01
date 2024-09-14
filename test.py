import unittest
from app import app


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    def test_predict(self):
        response = self.app.post('/predict', json={
            'CRIM': 0.1,
            'ZN': 0,
            'INDUS': 1.0,
            'CHAS': 0,
            'NOX': 0.5,
            'RM': 6.5,
            'AGE': 30.0,
            'DIS': 4.0,
            'RAD': 3,
            'TAX': 300,
            'PTRATIO': 15.0,
            'B': 350,
            'LSTAT': 5.0
        })
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
