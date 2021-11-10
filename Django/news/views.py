from django.shortcuts import get_object_or_404, render
from .models import News


# Create your views here.

def news_page(request):
    news=News.objects.all()
    
    return render(request, 'news.html', {'news':news})

def news_detail(request,slug):
    news = get_object_or_404(News, slug=slug)
    return render (request, 'news-detail.html', {'news':news})


