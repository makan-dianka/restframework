from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .. serializers.blog import BlogSerialiser
from .. models.blog import Blog
from django.shortcuts import get_object_or_404

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def blog_update(request, id):
    if request.method=='POST':
        post = get_object_or_404(Blog, pk=id)
        serialiser = BlogSerialiser(post, request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        return Response(serialiser.errors)