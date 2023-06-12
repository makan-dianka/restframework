from rest_framework.response import Response
from rest_framework.decorators import api_view
from .. serializers.blog import BlogSerialiser
from .. models.blog import Blog
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def blog_item(request, id):
    if request.method=='GET':
        post = get_object_or_404(Blog, pk=id)
        serializer = BlogSerialiser(post, many=False)
        return Response(serializer.data)