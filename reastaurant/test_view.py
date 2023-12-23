from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Menu, Booking, Category
from django.utils import timezone


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
        self.client.force_authenticate(user=self.admin_user)
        self.category = Category.objects.create(slug='test-category', title='Test Category')


    def test_menu_items_view(self):
        response = self.client.get('/api/menu') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_menu_view(self):
        # Test SingleMenuView with an authenticated user
        user = User.objects.create_user(username='user', password='userpass')
        self.client.force_authenticate(user=user)

        # Create a menu item
        menu_item = Menu.objects.create(title='Test Menu', price=10.0, category=self.category)
        response = self.client.get(f'/api/menu/{menu_item.id}')  # Adjust the URL according to your project's URL patterns
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booking_view(self):
        user = User.objects.create_user(username='user', password='userpass')
        self.client.force_authenticate(user=user)

        booking = Booking.objects.create(date=timezone.now().date(), time=timezone.now().time(), name="Ahmed")
        response = self.client.get('/api/bookings')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_index_view(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
