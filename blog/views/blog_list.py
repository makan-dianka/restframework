from rest_framework.response import Response
from rest_framework.decorators import api_view
from .. serializers.blog import BlogSerialiser
from .. models.blog import Blog

@api_view(['GET'])
def blog_list(request):
    if request.method=="GET":
        posts = Blog.objects.all()
        serialiser = BlogSerialiser(posts, many=True)
        return Response(serialiser.data)