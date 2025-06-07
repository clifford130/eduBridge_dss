from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_homepage_status_code(self):
        # The root path '/' is named 'home' in the 'core' app namespace
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse('core:home'))
        self.assertTemplateUsed(response, 'core/home.html')
        self.assertTemplateUsed(response, 'core/base.html') # Also check if base is used

    def test_homepage_contains_correct_content(self):
        response = self.client.get(reverse('core:home'))
        self.assertContains(response, "Welcome to EduBridge DSS")

    def test_homepage_uses_base_template_title_if_not_overridden(self):
        # This test assumes a view that doesn't override the title block
        # For our current HomePageView, it *does* override the title.
        # If we had a generic view using base.html without a title override,
        # it would inherit "EduBridge DSS" from base.html.
        # Let's test the actual title of the home page.
        response = self.client.get(reverse('core:home'))
        self.assertContains(response, "<title>Home - EduBridge DSS</title>")

# Example test for login page (add more as needed)
class LoginPageTests(TestCase):
    def test_login_page_status_code(self):
        response = self.client.get(reverse('login')) # 'login' is a global name from django.contrib.auth.urls
        self.assertEqual(response.status_code, 200)

    def test_login_page_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertTemplateUsed(response, 'core/base.html')

    def test_login_page_contains_login_form_elements(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, '<form method="post">')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, '<button type="submit" class="btn btn-primary">Login</button>')

# Example test for signup page
class SignupPageTests(TestCase):
    def test_signup_page_status_code(self):
        response = self.client.get(reverse('core:signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_uses_correct_template(self):
        response = self.client.get(reverse('core:signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertTemplateUsed(response, 'core/base.html')

    def test_signup_page_contains_signup_form_elements(self):
        response = self.client.get(reverse('core:signup'))
        self.assertContains(response, '<form method="post">')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, '<button type="submit" class="btn btn-primary">Sign Up</button>')
        self.assertContains(response, 'id_username') # Check for a field from UserCreationForm
        self.assertContains(response, 'id_password1') # Check for a field from UserCreationForm
        self.assertContains(response, 'id_password2') # Check for a field from UserCreationForm
