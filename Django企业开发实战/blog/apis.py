# from rest_framework import generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from blog.models import Post
# from blog.serializers import PostSerializer
#
#
# @api_view(["GET", "POST"])
# def post_list(request):
#     posts = Post.objects.filter(status=Post.STATUS_NORMAL)
#     post_serializers = PostSerializer(posts, many=True)
#     return Response(post_serializers.data)
#
#
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
#     serializer_class = PostSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from blog.models import Post
from blog.serializers import PostSerializer


# class PostViewSet(viewsets.ModelViewSet):
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    # permission_classes = [IsAdminUser]  # delete post put           因继承ReadOnlyModelViewSet，此项无用

    basename = 'api'

    def reverse_action(self, url_name, *args, **kwargs):
        """原生的reverse_action不支持  namespace的reverse"""

        super().reverse_action(url_name, *args, **kwargs)
