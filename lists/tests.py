from django.test import TestCase

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html_2(self):
        response = self.client.get("/")
        self.assertContains(response, "<title>To-Do lists</title>")
        self.assertContains(response, "<p>Add your first todo!</p>")
        self.assertContains(response, "<html>")
        self.assertContains(response, "</html>")