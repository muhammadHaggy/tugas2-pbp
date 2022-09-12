from django.test import TestCase

# Create your tests here.
class KatalogViewTest(TestCase):
    def test_view_url_exist(self):
        response = self.client.get('/katalog/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/katalog/')
        self.assertTemplateUsed(response, 'katalog.html')