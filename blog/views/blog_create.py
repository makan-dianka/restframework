from rest_framework.response import Response
from rest_framework.decorators import api_view
from .. serializers.blog import BlogSerialiser

@api_view(['POST'])
def blog_create(request):
    if request.method=='POST':
        serializer =  BlogSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)