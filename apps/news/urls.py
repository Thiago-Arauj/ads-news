from django.urls import path
from .views import NewsListView, NewsUpdateView, NewsCreateView, NewsDetailView
# não usados: ReadNewsView, HomeView, ListNewsByCategoryView
app_name = 'news'

urlpatterns = [
    path('item/<int:pk>/editar/', NewsUpdateView.as_view(), name='edit_news'),
    path('item/listar/', NewsListView.as_view(), name='list_news_admin'),
    path('noticias/adicionar/', NewsCreateView.as_view(), name='add_news'),
    path('noticia/<int:pk>/', NewsDetailView.as_view(), name='read_news'),
]
