from django.urls import include, path

from . import views
from .feeds import AtomSiteNewsFeed, LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path("detail/<slug:slug>/", views.post_detail, name="post_detail"),
    path("posts/category/<int:pk>/", views.post_category, name="post_category"),
    path("register/", views.register, name="register"),
]
