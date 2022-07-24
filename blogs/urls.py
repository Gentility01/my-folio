from django.urls import path
from .views import  blog_view, blog_detail

urlpatterns = [
    path('blog_view/', blog_view, name='blog_view'),
    path('blog_detail/<int:id>/', blog_detail, name='blog_detail'),
    # path('reply_comment/<int:id>/', reply_comment, name='reply_comment'),
    # path('reply_comment/<int:id>/', reply_comment, name='reply_comment'),
]


