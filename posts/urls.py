from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name="Post_Detail"),
    path('', PostList.as_view(), name="Post_List"),
    path('users/', UserList.as_view(), name = "User_List"),
    path('users/<int:pk>', UserDetail.as_view(), name = "User_Detail"),

]
