# zomato/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('/', views.display_menu, name='display_menu'),
    path('add_dish/', views.add_dish, name='add_dish')
]
