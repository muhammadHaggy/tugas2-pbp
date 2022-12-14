from django.test import TestCase

# Create your tests here.
class WatchlistViewTest(TestCase):
    def test_html_url_exist(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_json_url_exist(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    
    def test_xml_url_exist(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)