from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm


app_name = 'news'

urlpatterns = [
    path('details/<int:pk>', views.news_detail, name='news_detail'),
    path('predict/', views.predict, name='predict'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html', authentication_form=LoginForm), name='login'),
    path('', views.index),
]