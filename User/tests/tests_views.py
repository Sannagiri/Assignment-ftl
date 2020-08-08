from django.test import TestCase, Client
from django.urls import reverse
from User.models import *
import json

"""
-- Test case for the view of the API endpoint
"""

class Testview(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('User:detailviewpage')

    def tests_views(self):
        response = self.client.get(self.list_url)