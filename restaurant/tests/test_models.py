from django.test import TestCase

from restaurant.models import MenuItem, Booking  # Import your model



class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), 'IceCream : 80')



class BookingTest(TestCase):
    def test_get_book(self):
        item = Booking.objects.create(Name="IceCream", No_of_guests= 70, BookingDate="2025-02-26 22:25:00.000000")
        self.assertEqual(str(item), 'IceCream:70')


