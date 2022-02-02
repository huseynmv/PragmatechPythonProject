from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView, UserList, UserDetail

app_name = 'blog'
urlpatterns = [
    path('', BlogListAPIView.as_view(), name='blog'),
    path('<int:pk>', BlogDetailAPIView.as_view(), name='blog'),
    path('users', UserList.as_view(), name='user'),
    path('users/<str:first_name>', UserDetail.as_view(), name='user'),
    
    
    
]