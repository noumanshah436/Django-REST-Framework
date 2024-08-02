from rest_framework.response import Response
from rest_framework.views import APIView
from blogs.models import BlogPost
from blogs.serializers import BlogPostSerializer
from rest_framework import viewsets


# class BlogListView(APIView):

#     def get(self, request):
#         blogs = BlogPost.objects.all().order_by('publish_date')
#         serializer = BlogPostSerializer(blogs, many=True)
#         return Response({'status': 'SUCCESS', 'list': serializer.data})

class BlogModelViewset(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('publish_date')
    serializer_class = BlogPostSerializer