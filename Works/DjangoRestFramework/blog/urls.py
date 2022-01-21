from django.urls import path
from blog.views import template_blogs

app_name = 'blog'
urlpatterns = [
    path('', template_blogs, name='blog')
]