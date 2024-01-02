from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model

class PostViewsets(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class UserViewsets(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
