from django.test import TestCase
from django.urls import reverse

from .models import Student


class HomeViewTests(TestCase):
    def test_home_lists_students(self):
        Student.objects.create(first_name="Ana", last_name="Cruz", email="ana@example.com")
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ana Cruz")
        self.assertContains(response, "Student List")
