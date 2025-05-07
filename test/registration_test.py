import werkzeug
werkzeug.__version__ = "2.3.8"

import unittest
from app import app, db

class RegistrationTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:test_memory:'
        self.client = app.test_client()

        with app.app_context():
            db.create_all()
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_registration_success(self):
        response = self.client.post('/registration', data={
            'student_id': '12345',
            'email': 'test@example.com',
            'password': 'testpass',
            'confirm': 'testpass'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_registration_failure_missing_fields(self):
        response = self.client.post('/registration', data={
            'student_id': '12345',
            'email': '',
            'password': 'testpass',
            'confirm': 'testpass'
        }, follow_redirects=True)

        self.assertIn('This field is required.', response.data.decode())
        self.assertIn('email', response.data.decode())

    def test_registration_failure_invalid_credentials(self):
        """Test registration failure when student_id or email do not match existing records"""
        # Try to register with incorrect credentials (either student_id or email is wrong)
        response = self.client.post('/registration', data={
            'student_id': '99999',  # Invalid student_id that doesn't exist in the database
            'email': 'wrongemail@example.com',  # Invalid email that doesn't match any user
            'password': 'testpass',
            'confirm': 'testpass'
        }, follow_redirects=True)

        # Check that the form validation error for email is shown
        self.assertIn(b'Email must be the student university email ending with', response.data)

        # Alternatively, check that the student ID is invalid (in case the student_id format is also wrong)
        self.assertIn(b'Student ID must be between 7 and 8 digits', response.data)

        # Ensure we are still on the registration page and it's still rendering the form
        self.assertEqual(response.status_code, 200)

