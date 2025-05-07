import werkzeug
werkzeug.__version__ = "2.3.8"

import unittest
from flask import url_for
from flask_testing import TestCase
from app import app, db
from app.models import User, Task, Group, GroupTaskStatus
from app.forms import TaskForm
from flask_login import login_user

class TaskCreationTestCase(TestCase):
    def create_app(self):
        # Create and configure a new app instance for testing
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
        app.config['SECRET_KEY'] = 'secret'
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing purposes
        return app

    def setUp(self):
        # Create all tables in the test database
        db.create_all()

        # Create a test admin user
        self.admin_user = User(username='admin', email='admin@example.com', role='Admin', password='password')
        db.session.add(self.admin_user)

        # Create a test regular user
        self.regular_user = User(username='user', email='user@example.com', role='User', password='password')
        db.session.add(self.regular_user)

        # Commit users to the database
        db.session.commit()

        # Create a test group
        self.group = Group(name='Test Group')
        db.session.add(self.group)
        db.session.commit()

    def tearDown(self):
        # Remove all data after each test
        db.session.remove()
        db.drop_all()

    def test_create_task_non_admin(self):
        """Test non-admin users cannot access the task creation page"""
        # Log in as a regular user
        login_user(self.regular_user)

        # Try to access the create_task page
        response = self.client.get('/create_task')

        # Check if redirected to the home page
        self.assertRedirects(response, url_for('home'))

        # Check for the flash message indicating only admins can access the page
        with self.assertRaises(KeyError):  # Test that 'danger' flash message is set
            self.assertIn(b'Only admin users are allowed on that page', response.data)

    def test_create_task_admin(self):
        """Test task creation by an admin user"""
        # Log in as an admin user
        login_user(self.admin_user)

        # Create task form data
        task_data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'isUpload': False,
            'start_datetime': '2025-05-06 09:00:00',
            'end_datetime': '2025-05-06 17:00:00',
            'location': 'Test Location'
        }

        # Post request to create a new task
        response = self.client.post('/create_task', data=task_data, follow_redirects=True)

        # Check if the task was created successfully
        task = Task.query.filter_by(title='Test Task').first()
        self.assertIsNotNone(task)

        # Check for the success flash message
        self.assertIn(b'Task created successfully', response.data)

        # Check that the task is added to all groups (GroupTaskStatus entries are created)
        group_task_statuses = GroupTaskStatus.query.filter_by(task_id=task.id).all()
        self.assertEqual(len(group_task_statuses), 1)  # Assuming only one group was created in setup

    def test_create_task_form_validation_error(self):
        """Test form validation error when required fields are missing"""
        # Log in as an admin user
        login_user(self.admin_user)

        # Submit the form with missing data (e.g., title is missing)
        task_data = {
            'title': '',  # Empty title will cause validation error
            'description': 'Test Description',
            'isUpload': False,
            'start_datetime': '2025-05-06 09:00:00',
            'end_datetime': '2025-05-06 17:00:00',
            'location': 'Test Location'
        }

        # Post request to create a new task
        response = self.client.post('/create_task', data=task_data, follow_redirects=True)

        # Check if the form is re-rendered with validation errors
        self.assertIn(b'This field is required.', response.data)  # Assuming title is a required field


