from django.urls import path
from cars.views import *


app_name = 'car'
urlpatterns = [
    path('all/', CarsListView.as_view(), name='all_cars'),
    path('car/detail/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/create/', CarCreateView.as_view(), name='car_create'),
]