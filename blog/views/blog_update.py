from rest_framework.response import Response
from rest_framework.decorators import api_view
from .. serializers.blog import BlogSerialiser
from .. models.blog import Blog
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def blog_update(request, id):
    if request.method=='POST':
        post = get_object_or_404(Blog, pk=id)
        serialiser = BlogSerialiser(post, request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        return Response(serialiser.errors)