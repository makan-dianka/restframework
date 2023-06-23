from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .. serializers.blog import BlogSerialiser

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def blog_create(request):
    if request.method=='POST':
        serializer =  BlogSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)