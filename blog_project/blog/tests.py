from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

class BlogTests(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username='sourcecode',
			email='sourcecode@gmail.com',
			password='123sourcecode@'
		)

		self.post = Post.objects.create(
			title='A good title',
			body='nice body content',
			author=self.user
		)


	def test_string_representation(self):
		post = Post(title='A sample test')
		self.assertEqual(str(post), post.title) 

	def test_get_absolute_ulr(self):
		self.assertEqual(self.post.get_absolute_url(), '/post/1')

	def test_post_content(self):
		self.assertEqual(f'{self.post.title}', 'A good title')
		self.assertEqual(f'{self.post.author}', 'sourcecode')
		self.assertEqual(f'{self.post.body}', 'nice body content')


	def test_post_list_view(self):
		response = self.client.get('/homepage/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'nice body content')
		self.assertTemplateUsed(response, 'home.html')

	def test_post_detai_view(self):
		response = self.client.get('/post/1')
		self.assertEqual(response.status_code, 200)
		no_response = self.client.get('/post/1333')
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'A good title')
		self.assertTemplateUsed(response, 'post_detail.html')


	def test_post_create_view(self):

		response = self.client.post(reverse('post_new'), {
			'title':'new title',
			'body':'new body',
			'author':self.user,
		})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'new body')
		self.assertContains(response, 'new title')

	def test_post_update_view(self): # new
		response = self.client.post(reverse('post_edit', args='1'), {
		'title': 'Updated title',
		'body': 'Updated text',
		})
		self.assertEqual(response.status_code, 302)
		
	def test_post_delete_view(self): # new
		response = self.client.post(
		reverse('post_delete', args='1'))
		self.assertEqual(response.status_code, 302)















	

