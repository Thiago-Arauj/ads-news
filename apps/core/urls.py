from django.urls import path
from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<uuid:pk>/', views.read_news, name='read_news'),
]

