from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.api.serializers import BlogSerializer
from blog.models import Blog

@api_view(['GET'])
def blog_list_create(request):
    blog = Blog.objects.all()
    serializer = BlogSerializer(blog, many = True)
    return Response(serializer.data)