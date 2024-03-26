from django.test import TestCase
from .models import Post
from django.urls import reverse


class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(title='django demo', author='Mr Dee', slug='django-demo')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django demo')

    def test_say_something(self):
        response = self.client.get(reverse('saySomething'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 
                            '<h1 style="color:green">What is wrong with the leaders of today?</h1>', 
                            html=True)
