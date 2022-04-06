from django.db import models

# my imports below
from django.urls import (
    reverse,
)  # will allow reference to an object by its URL template name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    # user can be the author of many different blog posts but not the other way around (below)
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE
    )  # will create a many-to-one relationship
    body = models.TextField()

    # provide human readable version of the model in the admin or Django shell
    def __str__(self):
        return self.title

    # tells Django how to calculate the canonical URL for our model object
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
