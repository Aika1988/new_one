from rest_framework import generics
from applications.post.models import Post
from applications.post.serializers import PostSerializer

# class PostListAPIView(generics.ListAPIView): # get запрос
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostCreateAPIView(generics.CreateAPIView): # create запрос
#     serializer_class = PostSerializer    


# class PostUpdateAPIView(generics.UpdateAPIView): # update запрос
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDeleteAPIView(generics.DestroyAPIView): # запрос для удаления
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetailAPIView(generics.RetrieveAPIView): # запрос для поиска деталей
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'id'


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer







