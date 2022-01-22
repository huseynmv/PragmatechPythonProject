from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView

app_name = 'blog'
urlpatterns = [
    path('', BlogListAPIView.as_view(), name='blog'),
    path('<int:pk>', BlogDetailAPIView.as_view(), name='blog')
    
]