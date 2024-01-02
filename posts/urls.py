from django.urls import path
from .views import PostViewsets, UserViewsets
from rest_framework.routers import SimpleRouter

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name="Post_Detail"),
#     path('', PostList.as_view(), name="Post_List"),

#     path('users/', UserList.as_view(), name = "User_List"),
#     path('users/<int:pk>', UserDetail.as_view(), name = "User_Detail"),

# ]
router = SimpleRouter()
router.register("users", UserViewsets, basename="users")
router.register("posts", PostViewsets, basename="posts")
urlpatterns = router.urls
