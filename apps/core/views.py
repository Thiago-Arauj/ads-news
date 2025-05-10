from django.shortcuts import render
from apps.news.models import News

def main(request):
    news= News.objects.all()
    return render(request, 'home.html', {'news': news})