#define URL route for index() view
from django.urls import path,include
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-items-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item-retrieve-update-delete'),
    path('menu-itmes/',views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/',views.SingleMenuItemView.as_view()),

]
