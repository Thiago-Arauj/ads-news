from django.shortcuts import render
from apps.news.models import News
from django.contrib.auth.decorators import login_required

def main(request):
    news= News.objects.all()
    return render(request, 'home.html', {'news': news})

#exemplo de uma página que requer autenticação
#@login_required
# def main(request):
#     news= News.objects.all()
#     return render(request, 'home.html', {'news': news})