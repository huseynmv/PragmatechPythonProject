from .serializers import BlogSerializer
from blog.models import Blog
from django.http import HttpResponse, JsonResponse

def blog_api(request):
    blogs = Blog.objects.all()
    serializers = BlogSerializer(blogs, many = True)
    return JsonResponse(serializers.data, safe=False)