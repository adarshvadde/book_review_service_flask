import unittest
import sys
import os
from unittest.mock import patch

# Add app to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.extensions import db

class CacheIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.drop_all()
            db.create_all()

    @patch('app.routes.cache.get', return_value=None)
    @patch('app.routes.cache.set')  # You can assert this was called if needed
    def test_cache_miss_then_db_fetch(self, mock_cache_set, mock_cache_get):
        # Create a book to ensure DB has data
        self.client.post('/books', json={'title': 'Cache Test Book'})

        # First request triggers cache miss and should hit DB
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        books = response.get_json()
        self.assertTrue(any(b['title'] == 'Cache Test Book' for b in books))

        # Confirm cache.get was called and returned None (cache miss)
        mock_cache_get.assert_called_once()
        # Confirm cache.set was called to populate Redis
        mock_cache_set.assert_called_once()

    @patch('app.routes.cache.get', side_effect=Exception("Redis down"))
    def test_cache_failure_handling(self, mock_cache_get):
        # Add a book so DB has data
        self.client.post('/books', json={'title': 'Fallback Book'})

        # Simulate Redis failure
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        books = response.get_json()
        self.assertTrue(any(b['title'] == 'Fallback Book' for b in books))

        # Redis threw error, but app should still return data
        mock_cache_get.assert_called_once()

if __name__ == '__main__':
    unittest.main()
