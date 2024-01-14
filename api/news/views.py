from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from news.models import News

# Create your views here.
# def get_news(request):
#     return render(request, 'news.html')

def index(request):
    news = News.objects.all()
    return render(request, 'index.html', {
        'news': news,
    })

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news.html', {
        'news': news,
    })