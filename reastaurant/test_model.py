from django.test import TestCase
from .models import Category, Menu, Booking
from django.utils import timezone

class ModelsTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(slug='test-category', title='Test Category')
        self.menu_item = Menu.objects.create(title='Test Menu Item', price=9.99, category=self.category)
        self.booking = Booking.objects.create(name='Test Booking', date=timezone.now().date(), time=timezone.now().time())

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_menu_str_method(self):
        self.assertEqual(str(self.menu_item), 'Test Menu Item')

    def test_booking_str_method(self):
        self.assertEqual(str(self.booking), 'Test Booking')


