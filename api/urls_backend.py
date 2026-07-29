
from django.urls import path,include
from . import views

urlpatterns = [
    path('homesApi/', views.HomeViewSet.as_view({'get': 'list', 'post': 'create'}), name='home-list'),
    path('homesApi/<int:pk>/', views.HomeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='home-detail'),
]