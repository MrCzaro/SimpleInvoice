from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.test import TestCase


class CustomUserModelTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="test@django.com", username="test_user", password="test_password123")
        self.assertEqual(user.email, "test@django.com")
        self.assertEqual(user.username, "test_user")
        self.assertTrue(user.check_password("test_password123"))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="test@django.com", username="test_admin", password="admin_password123")
        self.assertEqual(admin_user.email, "test@django.com")
        self.assertEqual(admin_user.username, "test_admin")
        self.assertTrue(admin_user.check_password("admin_password123"))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_email_unique(self):
        User = get_user_model()
        User.objects.create_user(email="test@django.com", username="test_user", password="test_password123")
        with self.assertRaises(IntegrityError):
            User.objects.create_user(email="test@django.com", username="test_user", password="test_password123")


    def test_username_required(self):
        User = get_user_model()
        with self.assertRaises(ValueError):
            User.objects.create_user(email="test@django.com", username="", password="test_password123")


    def test_user_id_is_uuid(self):
        User = get_user_model()
        user = User.objects.create_user(email="test@django.com", username="test_user", password="test_password")
        self.assertIsNotNone(user.id)
        self.assertEqual(len(str(user.id)), 36)  # UUID length

    