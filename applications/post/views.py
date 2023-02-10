from rest_framework import generics
from applications.post.models import Post
from applications.post.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from applications.post.permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.pagination import PageNumberPagination


# class CustomPagination():
#     page_size = 1
#     page_size_query_param = 'page_size'
#     max_page_size = 10000


# CRUD на классах
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


# CRUD только двумя способами
class PostListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = ['owner', 'title']
    search_fields = ['title'] 
    ordering_fields = ['id', 'owner']

    # так можно переопределять queryset чтобы получить страницу по владельцу(фильтрация страниц)
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # queryset = queryset.filter(owner=2)
    #     # print(self.request.query_params)
    #     filter_owner = self.request.query_params.get('owner')
    #     if filter_owner:
    #         queryset = queryset.filter(owner=filter_owner)
    #     return queryset

    def perform_create(self, serializer): # чтобы вызвать сериалайзер
        serializer.save(owner=self.request.user)

class PostDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer







