from django.shortcuts import render
from .models import Blog
# Create your views here.

def blog_page(request):
    blog = Blog.objects.all()
    return render (request, 'blog.html', {'blog':blog})