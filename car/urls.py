from django.urls import path
from .import views

urlpatterns = [
    path('add/', views.AddPostCreateView.as_view(), name='sell_car'),
    path('buy_car/<int:id>/', views.car_view, name='car_view'),
    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_car'),
]