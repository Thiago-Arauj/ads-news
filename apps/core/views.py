from django.shortcuts import get_object_or_404, render
from apps.news.models import News, Category
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import ContextMixin

# exemplo de uma página que requer autenticação
# @login_required
# def main(request):
#     news= News.objects.all()
#     return render(request, 'home.html', {'news': news})

class CommonContextMixin(ContextMixin): 
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs) or {}
            sponsored_news = News.objects.filter(is_sponsored=True).order_by('-created_at')[:3] 
            most_read_news = News.objects.all().order_by('-views')[:5]            
            context['most_read_news'] = most_read_news
            context['sponsored_news'] = sponsored_news
            context['categories'] = News.CategoryChoices.choices
            return context

class HomeView(CommonContextMixin, TemplateView):  
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            carousel_news = News.objects.filter(in_carousel=True).order_by('-created_at')[:3] 
            featured = News.objects.filter(is_featured=True).order_by('-created_at')[:7]       
            list_news = News.objects.all()[:5]
            videos = News.objects.all()[:3] 
           
            featured_news = featured[:3] if len(featured) > 2 else None
            featured_news_2 = featured[3:] if len(featured) > 3 else None

            news = {
                'carousel_news': carousel_news,
                'featured_news': featured_news,
                'featured_news_2': featured_news_2,
                'list_news': list_news,
            }
            
            context['news'] = news
            context['videos'] = videos
            
            return context
    
class ReadNewsView(CommonContextMixin, DetailView):
    model = News
    template_name = 'read_news.html'
    context_object_name = 'featured'  

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)


        obj.views += 1
        obj.save(update_fields=['views'])

        return obj

class ListNewsView(CommonContextMixin, ListView):
    model = News
    template_name = 'list_news.html'
    context_object_name = 'news_by_category'
    paginate_by = 6

    def get_queryset(self):
        queryset = News.objects.all()
        search = self.request.GET.get('search')
        order_by = self.request.GET.get('order_by')

        if search:
            queryset = queryset.filter(title__icontains=search)
        
        if order_by:
            queryset = queryset.order_by(order_by)        
        
        return queryset
    
class ListNewsByCategoryView(CommonContextMixin, ListView):
    model = News
    template_name = 'list_news.html'
    context_object_name = 'news_by_category'
    paginate_by = 6

    def get_queryset(self):
        queryset = News.objects.all()
        search = self.request.GET.get('search')
        order_by = self.request.GET.get('order_by')
        category_id = self.kwargs.get('category_id')  

        if category_id:            
            queryset = queryset.filter(category_name=category_id)

        if search:
            queryset = queryset.filter(title__icontains=search)
        
        if order_by:
            queryset = queryset.order_by(order_by)        
        
        return queryset
