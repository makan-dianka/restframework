from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .. models.blog import Blog
from django.shortcuts import get_object_or_404

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def blog_delete(request, id):
    post = get_object_or_404(Blog, pk=id)
    post.delete()
    return Response({'post' : 'deleted success'})