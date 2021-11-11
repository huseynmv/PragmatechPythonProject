from django.urls import path
from .views import news_page, news_detail

app_name = 'news'

urlpatterns = [
    path('', news_page, name='news'),
    path('news-detail/<slug:slug>/', news_detail, name='news-detail' ),
]
