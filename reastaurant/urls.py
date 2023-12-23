from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('bookings', views.BookingView.as_view(), name='bookings'),
    path('', views.index, name='home')
]