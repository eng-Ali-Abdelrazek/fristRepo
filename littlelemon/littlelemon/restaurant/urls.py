#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-items-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item-retrieve-update-delete'),
]
