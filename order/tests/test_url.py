from django.test import TestCase
from django.urls import reverse, resolve
from order.views import create_order

class TestOrderUrls(TestCase):
    def test_create_order_url(self):
        url = reverse('create_order')
        self.assertEqual(resolve(url).func, create_order)