from django.shortcuts import render

# ListCreateAPIView(built-in) -> read-write endpoint(POST request and READ request) 
# RetrieveUpdateDestroyAPIView(built-in generics)-> CRUD

from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListAPIView):
    #
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    #
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer