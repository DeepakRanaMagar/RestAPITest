from django.shortcuts import render

# ListCreateAPIView(built-in) -> read-write endpoint(POST request and READ request) 
# RetrieveUpdateDestroyAPIView(built-in generics)-> CRUD

from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, permissions

class PostList(generics.ListCreateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        permissions.IsAdminUser,
    )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    