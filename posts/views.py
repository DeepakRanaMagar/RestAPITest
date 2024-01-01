from django.shortcuts import render

# ListCreateAPIView(built-in) -> read-write endpoint(POST request and READ request) 
# RetrieveUpdateDestroyAPIView(built-in generics)-> CRUD

from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    