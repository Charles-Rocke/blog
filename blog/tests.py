from django.test import TestCase

# my imports
from django.contrib.auth import get_user_model  # to refer to our user
from .models import Post
from django.urls import reverse

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    # set up data for a test user and a test post
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        cls.post = Post.objects.create(
            title="A test title",
            body="Nice test content",
            author=cls.user,
        )

    # all tests are focused on the 'Post' model so our test name is test_post_model
    def test_post_model(self):
        self.assertEqual(self.post.title, "A test title")
        self.assertEqual(self.post.body, "Nice test content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A test title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    # Tests for generic functionality (same as previous practice apps)
    # test correct url list view
    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # test url location detail view
    def test_url_exists_at_location_detailview(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    # test post list view
    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice test content")
        self.assertTemplateUsed(response, "home.html")

    # test post detail view
    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A test title")
        self.assertTemplateUsed(response, "post_detail.html")

    # test post create view
    def test_post_createview(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "New title",
                "body": "body boi",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)  # 302 is a redirect status code
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "body boi")

    # test post update view
    def test_post_updateview(self):
        response = self.client.post(
            reverse(
                "post_edit",
                args="1",
            ),
            {"title": "updated title", "body": "updated body"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "updated title")
        self.assertEqual(Post.objects.last().body, "updated body")

    # test delete view
    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
