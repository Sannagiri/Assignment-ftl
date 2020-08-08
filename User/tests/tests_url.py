from django.test import SimpleTestCase
from django.urls import resolve,reverse
from User.views import *


"""
-- Test case for checking the url is routing to the desired endpoint
"""
class Testurls(SimpleTestCase):
    def tests_urls(self):
        url = reverse('User:detailviewpage')
        print(resolve(url))
        self.assertEquals(resolve(url).func, userdetailview)

