from django.test import SimpleTestCase
from django.urls import reverse

class SimpleTests(SimpleTestCase):
	
	def test_hompage(self):

		response = self.client.get(reverse('pages:home'))
		self.assertEqual(response.status_code, 200)

	def test_aboutpage(self):
		response = self.client.get(reverse('pages:about')) 
		self.assertEqual(response.status_code, 200)



