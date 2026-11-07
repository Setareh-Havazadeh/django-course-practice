from django.urls import path
from blog.views import *

app_name = "blog"

urlpatterns = [
    path('', bloghome_view, name='blog-home'),
    path('single', blogsingle_view, name='blog-single'),
]
