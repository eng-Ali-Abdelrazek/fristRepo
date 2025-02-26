from django.shortcuts import render
from .serializers import MenuSerializer,BookingSerializer,MenuItemSerializer
from rest_framework import generics
from .models import Menu,Booking,MenuItem
from rest_framework import viewsets


from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'index.html')


# View to list and create menu items
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# View to retrieve, update and delete a single menu item
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  # Require authentication


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer