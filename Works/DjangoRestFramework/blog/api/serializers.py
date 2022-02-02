from dataclasses import field
from rest_framework import serializers
from blog.models import Blog, User


# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
    
#     def create(self, validated_data):
#         return Blog.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.save()
#         return instance



class Userserializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email')

class BlogSerializer(serializers.ModelSerializer):
    
    author = Userserializer()
    
    class Meta:
        model = Blog
        exclude = ('id',)
        # fields = '__all__'
    
    