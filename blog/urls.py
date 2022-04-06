from django.urls import path
from .views import BlogListView, BlogDetailView

# url patterns
urlpatterns = [
    # all entries start with post/, the primary key is represented by an integer
    path("", BlogListView.as_view(), name = "home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name = "post_detail")
]