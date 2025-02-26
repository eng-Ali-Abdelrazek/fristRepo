# serializers.py
from rest_framework import serializers
from .models import Menu, Booking,MenuItem

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'Title', 'Price', 'Inventory']


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields= '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
