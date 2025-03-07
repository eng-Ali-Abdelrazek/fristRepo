#define URL route for index() view
from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.index, name='index'),
    path('menu-itmes/',views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/',views.SingleMenuItemView.as_view()),

]
