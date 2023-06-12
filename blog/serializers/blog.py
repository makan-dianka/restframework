from rest_framework import serializers
from .. models.blog import Blog

class BlogSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'body']