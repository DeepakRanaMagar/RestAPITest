from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name="Post_Detail"),
    path('', PostList.as_view(), name="Post_List"),
]
