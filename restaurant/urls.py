from django.contrib import admin 
from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path('menu/items/', views.MenuItemsView.as_view(), name="menu-list"),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view()),
]