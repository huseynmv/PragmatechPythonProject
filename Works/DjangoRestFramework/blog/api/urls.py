from django.urls import path
from .views import blog_api

app_name = 'blog'
urlpatterns = [
    path('', blog_api, name='blog')
]