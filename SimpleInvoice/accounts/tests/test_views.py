from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class SignupUserViewTest(TestCase):
    def test_successful_rendering(self):
        response = self.client.get(reverse("accounts:signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts.html")
        
    def test_context_data(self):
        response = self.client.get(reverse("accounts:signup"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertIn("title", response.context)

    def test_successful_account_creation(self):
        data = {
            "username": "Test_user",
            "email": "test@django.com",
            "password1": "test_password123",
            "password2": "test_password123",

        }
        User = get_user_model()
        response = self.client.post("/accounts/signup/", data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("accounts:login"))
        # Check if a user was created:
        self.assertTrue(User.objects.filter(email=data["email"]).exists())
    
    def incorrect_email(self):
        data = {
            "username": "Test_user",
            "email": "testatdjango.com",
            "password1": "test_password123",
            "password2": "test_password123",

        }
        response = self.client.post("/accounts/signup/", data)
        self.assertEqual(response.status_code, 302)
        self.assertFormError(response, "form", "email", ["Enter a valid email address."])
        
        
class LoginViewTest(TestCase):
    @classmethod
    def setUp(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(
            username="Test_user",
            email="testatdjango.com",
            password="test_password123",
        )

    def test_successful_rendering(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts.html")
        self.assertIn("form", response.context)
        self.assertIn("title", response.context)

    def test_successful_login(self):
        response = self.client.post("/accounts/login/", {"username": "testatdjango.com", "password": "test_password123"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("invoice:dashboard"))

    def test_post_request_invalid_credentials(self):
        response = self.client.post(reverse("accounts:login"), {"username": "testatdjango.com", "password": " "})
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, "accounts.html")

    def test_post_request_invalid_form(self):
        response = self.client.post(reverse("accounts:login"), {"username": "test@django.com", "password": ""})
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, "accounts.html")

        
class LogoutUserViewTest(TestCase):
    def test_logout(self):
        User = get_user_model()
        User.objects.create_user(
            username="Test_user",
            email="test@django.com",
            password="test_password123",
        )
        self.client.login(email="test@django.com", password="adminpassword")
        response = self.client.get(reverse("accounts:logout"))
        self.assertRedirects(response, reverse("accounts:login"))
        self.assertFalse(response.wsgi_request.user.is_authenticated)