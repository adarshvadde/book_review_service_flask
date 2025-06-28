import unittest
import sys
import os

# Fix module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.extensions import db

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def test_add_and_get_book(self):
        self.client.post('/books', json={'title': 'Test Book'})
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.get_json()) > 0)

if __name__ == '__main__':
    unittest.main()
