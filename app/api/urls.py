from django.urls import path
from .views.category_views import (
    CategoryDetailView,
    CategoryCreateView,
    CategoryListView,
    CategoryUrlHandleView,
    CategoryCountView
)
from .views.blog_post_views import (
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostListView,
    BlogPostUrlHandleView,
    BlogPostCountView
)
from .views.blog_image_views import (
    UploadBlogImageView,
    BlogImageListView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views.user_views import RegisterUserView




urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/count/', CategoryCountView.as_view(), name='category-count'),
    path('categories/<uuid:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/urlhandle/<str:url_handle>/', CategoryUrlHandleView.as_view(), name='category-by-url'),

    path('blogposts/', BlogPostListView.as_view(), name='blog-post-list'),
    path('blogposts/create/', BlogPostCreateView.as_view(), name='blog-post-create'),
    path('blogposts/count/', BlogPostCountView.as_view(), name='blog-post-count'),
    path('blogposts/<uuid:id>/', BlogPostDetailView.as_view(), name='blog-post-detail'),
    path('blogposts/urlhandle/<str:url_handle>/', BlogPostUrlHandleView.as_view(), name='blog-post-by-url'),

    path('images/', BlogImageListView.as_view(), name='blog-image-list'),
    path('images/upload/', UploadBlogImageView.as_view(), name='upload-blog-image'),

    path('auth/register/', RegisterUserView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]