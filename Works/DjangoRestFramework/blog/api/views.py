from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from blog.api.serializers import BlogSerializer
from blog.models import Blog

@api_view(['GET', 'POST',])
def blog_list_create(request):
    
    if request.method == 'GET':
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (status=status.HTTP_400_BAD_REQUEST, message = {'message': 'Bad request message'})