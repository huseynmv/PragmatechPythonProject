from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . models import Blog



def template_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})