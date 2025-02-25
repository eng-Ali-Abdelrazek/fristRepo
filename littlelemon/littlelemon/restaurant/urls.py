#define URL route for index() view
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-items-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item-retrieve-update-delete'),

]
