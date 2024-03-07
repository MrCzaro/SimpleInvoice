
from django.test import TestCase

from accounts.forms import CustomAuthenticationForm, CustomUserCreationForm

class CustomAuthenticationFormTest(TestCase):
    def test_form_labels(self):
        form = CustomAuthenticationForm()
        self.assertEqual(form.fields["username"].label, "Email address")
        self.assertEqual(form.fields["password"].label, "Password")

    def test_form_widget_classes(self):
        form = CustomAuthenticationForm()
        self.assertIn("form-class", form.fields["username"].widget.attrs["class"])
        self.assertIn("form-class", form.fields["password"].widget.attrs["class"])
        
class CustomUserCreationFormTest(TestCase):
    def test_form_labels(self):
        form = CustomUserCreationForm()
        self.assertEqual(form.fields["username"].label, "Username")
        self.assertEqual(form.fields["email"].label, "Email address")
        self.assertEqual(form.fields["password1"].label, "Password")
        self.assertEqual(form.fields["password2"].label, "Confirm password")

    def test_form_widget_classes(self):
        form = CustomUserCreationForm()
        self.assertIn("form-class", form.fields["username"].widget.attrs["class"])
        self.assertIn("form-class", form.fields["email"].widget.attrs["class"])
        self.assertIn("form-class", form.fields["password1"].widget.attrs["class"])
        self.assertIn("form-class", form.fields["password2"].widget.attrs["class"])