from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate-flow/', views.calculate_flow, name='calculate_flow'),
]
