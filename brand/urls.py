from django.urls import path
from .import views
urlpatterns = [
    path('add/', views.car_brand ,name='car_brand'),
]