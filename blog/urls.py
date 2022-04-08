from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

# url patterns
urlpatterns = [
    # all entries start with post/, the primary key is represented by an integer
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
]
