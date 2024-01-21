from django.shortcuts import get_object_or_404, render
from news.models import News
from news.predictions_service import get_prediction, load_model, load_vector

def index(request):
    news = News.objects.all()
    return render(request, 'index.html', {
        'news': news,
    })

def news_detail(request, pk):
    model = load_model()
    vector = load_vector()
    news = get_object_or_404(News, pk=pk)

    news.prediction = get_prediction(model, vector, news.content)
    
    return render(request, 'news.html', {
        'news': news,
    })

def predict(request):
    model = load_model()
    vector = load_vector()
    news_detail = request.GET.get('q','')
    prediction = get_prediction(model, vector, news_detail)
    return render(request, 'predictions.html', {
        'prediction': prediction,
    })