from django.urls import path
from .views import ListNewsView, ReadNewsView, HomeView, ListNewsByCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/<uuid:pk>/', ReadNewsView.as_view(), name='read_news'),
    path('news/', ListNewsView.as_view(), name='list_news'),
    path(
        'news/category/<str:category_id>/',
        ListNewsByCategoryView.as_view(),
        name='list_news_by_category'
    ),
]
