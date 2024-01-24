from django.shortcuts import get_object_or_404, render
from news.models import News
from news.predictions_service import get_prediction
from news.forms import SignupForm, AddNewsForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index(request):
    query = request.GET.get('query','')
    news = News.objects.all().order_by('published')

    if query:
        news = news.filter(prediction__exact=query)

    return render(request, 'index.html', {
        'news': news,
        'query': query,
    })

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    
    return render(request, 'news.html', {
        'news': news,
    })

def predict(request):
    news_detail = request.GET.get('predict','')
    prediction = get_prediction(news_detail)
    return render(request, 'predictions.html', {
        'prediction': prediction,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form,
    })

@login_required
def addNews(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.publishedBy = request.user
            item.prediction = get_prediction(item.content)
            item.save()

            return redirect('/news/')
    else:
        form = AddNewsForm()

    return render(request, 'add_news.html', {
        'form': form,
    })