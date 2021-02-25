from django.urls import path
from . import views

urlpatterns = [
    path('<int:flight_id>', views.flight, name='flight'),
    path('new_index/', views.__index),
    path('airline/', views.new_index),
    path('', views.index, name='index'),
    path('<int:flight_id>/book', views.book, name='book')
]
