import unittest
from src.app import create_app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_get_meta(self):
        response = self.client.get('/meta')
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', response.json)
        self.assertIn('version', response.json)
        self.assertIn('buid', response.json)

if __name__ == '__main__':
    unittest.main()