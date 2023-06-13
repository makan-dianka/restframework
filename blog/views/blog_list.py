from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .. serializers.blog import BlogSerialiser
from .. models.blog import Blog

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def blog_list(request):
    if request.method=="GET":
        posts = Blog.objects.all()
        serialiser = BlogSerialiser(posts, many=True)
        return Response(serialiser.data)