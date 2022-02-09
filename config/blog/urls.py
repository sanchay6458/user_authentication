from django.urls import path
from .views import blogs,  blog_detail , BlogCreateView , BlogUpdateView, BlogDeleteView,my_blogs, blog_details

urlpatterns = [
    path('', blogs, name='blogs'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('blog/<int:blog_id>/', blog_details, name='blog_details'),
    path('blogs/blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/<int:pk>/edit/',BlogUpdateView.as_view(), name='blog_edit'),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'), #new
    path('my_blogs/', my_blogs, name='my_blogs'),
]