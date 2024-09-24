from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
	def setUp(self):
		Post.objects.create(text='just a test')

	def test_text_content(self):
		post = Post.objects.get(id=1)
		expected_object_name = f'{post.text}'
		self.assertEqual(expected_object_name, 'just a test')

class HomePageViewTest(TestCase):
	
	def setUp(self):
		Post.objects.create(text='another text')

	def test_view_url_location(self):
		resp = self.client.get('/homepage/')
		self.assertEqual(resp.status_code, 200)


	def test_view_url_name(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)


	def test_viewTemplate(self):

		resp = self.client.get('/homepage/')
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'home.html')


