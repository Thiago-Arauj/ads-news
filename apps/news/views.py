from django.shortcuts import render
from django.urls import reverse_lazy
from .models import News
from apps.core.views import CommonContextMixin
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from apps.news.utils.translator import translate_this
# Chamem essa função para traduzir os textos dinamicamente


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail_news.html'
    context_object_name = 'news'

class NewsCreateView(CreateView):
    model = News
    fields = ['category_name', 'title', 'abstract', 'content', 'image', 'in_carousel', 'is_featured', 'is_sponsored']
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('list_news')


class NewsUpdateView(UpdateView):
    model = News
    fields = ['category_name', 'title', 'abstract', 'content', 'image', 'in_carousel', 'is_featured', 'is_sponsored']
    template_name = 'news/edit_news.html'
    success_url = reverse_lazy('list_news')


class NewsListView(ListView):
    model = News
    template_name = 'news/list_news.html'
    context_object_name = 'page_obj'
    paginate_by = 6
    ordering = ['-created_at']


class EditNews(CommonContextMixin, UpdateView):
    model = News
    template_name = 'list_news.html'
    context_object_name = 'edit_news'


class DeleteNews(CommonContextMixin, DeleteView):
    model = News
    template_name = 'list_news.html'
    context_object_name = 'delete_news'

