from django.test import TestCase
from django.shortcuts import reverse


class HelloViewTests(TestCase):
	def test_postslist_page(self):
		response = self.client.get(reverse("Home_page"))
		self.assertEqual(response.status_code, 200)

