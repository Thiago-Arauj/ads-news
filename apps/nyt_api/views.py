from django.shortcuts import render
from django.http import JsonResponse
from .api import get_news


# Create your views here.
def root(request):
    return JsonResponse({'mensagem': get_news()})
