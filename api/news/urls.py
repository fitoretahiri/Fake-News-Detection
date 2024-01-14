from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('details/<int:pk>', views.news_detail, name='news_detail'),
    path('', views.index),
]