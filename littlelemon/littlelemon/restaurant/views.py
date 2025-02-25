from django.shortcuts import render
from .serializers import MenuSerializer,BookingSerializer
from rest_framework import generics
from .models import Menu,Booking
from rest_framework import viewsets

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