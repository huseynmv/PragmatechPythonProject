from django.urls import path
from .views import news_page

app_name = 'news'

urlpatterns = [
    path('', news_page, name='news'),
]
