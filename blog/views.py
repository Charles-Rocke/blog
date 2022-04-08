from django.shortcuts import render

# my imports
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy  # redirect to another page

# Create your views here.

# blog list view
class BlogListView(ListView):
    model = Post
    template_name = "home.html"


# detail page
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


# create page
class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


# update page
class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


# delete page
class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")  # redirect to another page
