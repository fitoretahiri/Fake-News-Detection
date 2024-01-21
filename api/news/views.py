from django.shortcuts import get_object_or_404, render
from news.models import News
from news.predictions_service import make_prediction, load_model, load_vector

def index(request):
    news = News.objects.all()
    return render(request, 'index.html', {
        'news': news,
    })

def news_detail(request, pk):
    model = load_model()
    vector = load_vector()
    news = get_object_or_404(News, pk=pk)

    prediction = make_prediction(model, vector, news.content)
    if prediction[0] == 1:
        news.prediction = 'reliable'
    else:
        news.prediction = 'not reliable'
    
    return render(request, 'news.html', {
        'news': news,
    })