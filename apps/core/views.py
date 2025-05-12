from django.shortcuts import get_object_or_404, render
from apps.news.models import News
from django.contrib.auth.decorators import login_required

# exemplo de uma página que requer autenticação
# @login_required
# def main(request):
#     news= News.objects.all()
#     return render(request, 'home.html', {'news': news})


def home(request):
    news = News.objects.all()
    carousel = News.objects.filter(in_carousel=True).order_by('-created_at')[:3]
    featured = News.objects.filter(is_featured=True).order_by('-created_at')[:7]
    sponsored = News.objects.filter(is_sponsored=True).order_by('-created_at')[:3]
    most_read = News.objects.all().order_by('-views')[:5]

    featured1 = featured[0] if len(featured) > 0 else None
    featured2 = featured[1] if len(featured) > 1 else None
    featured3 = featured[2] if len(featured) > 2 else None
    featureds = featured[3:] if len(featured) > 3 else []

    news = {
        'carousel': carousel,
        'featured1': featured1,
        'featured2': featured2,
        'featured3': featured3,
        'featureds': featureds,
        'most_read': most_read,
        'sponsored': sponsored,
    }

    return render(request, 'home.html', {'news': news})


def read_news(request, pk):
    featured_news = get_object_or_404(News, id=pk)
    sponsored = News.objects.filter(is_sponsored=True).order_by('-created_at')[:3]
    most_read = News.objects.all().order_by('-views')[:5]

    featured_news.views += 1
    featured_news.save()

    news = {
        'featured': featured_news,
        'most_read': most_read,
        'sponsored': sponsored,
    }

    return render(request, 'read_news.html', {'news': news})
