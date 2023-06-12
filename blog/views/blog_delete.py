from rest_framework.response import Response
from rest_framework.decorators import api_view
from .. serializers.blog import BlogSerialiser
from .. models.blog import Blog
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def blog_delete(request, id):
    post = get_object_or_404(Blog, pk=id)
    post.delete()
    return Response({'post' : 'deleted success'})