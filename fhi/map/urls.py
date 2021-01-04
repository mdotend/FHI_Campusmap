from django.urls import path

from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('test', views.index, name='test'),
    path('plants/',views.plants, name='plants'),
]