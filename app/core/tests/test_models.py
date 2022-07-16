"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test models."""

    def test_create_user_with_email_succesful(self):
        """Test creatin a user with an email is succesful"""
        email = 'test@example.com'  # example.com wird standartmässig für test verwendet
        password = 'testpass123'
        # rufe get_user_model-Methode auf und übergebe email sowie passwort
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))