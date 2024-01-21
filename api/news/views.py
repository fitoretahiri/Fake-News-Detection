from django.shortcuts import get_object_or_404, render
from news.models import News
from news.predictions_service import get_prediction

def index(request):
    news = News.objects.all()
    return render(request, 'index.html', {
        'news': news,
    })

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)

    news.prediction = get_prediction(news.content)
    
    return render(request, 'news.html', {
        'news': news,
    })

def predict(request):
    news_detail = request.GET.get('predict','')
    prediction = get_prediction(news_detail)
    return render(request, 'predictions.html', {
        'prediction': prediction,
    })