from django.contrib.auth.models import User
from django.db import models


CATEGORYCHOICES = (
    ("TECHNOLOGY","TECHNOLOGY"),
    ("INFORMATION","INFORMATION"),
    ("DATASCIENCE","DATASCIENCE"),
    ("AI","ARTIFICIAL INTELLIGENCE"),
    ("ML","MACHINE LEARNING"),
    ("SECURITY","CYBER SECURITY"),
    ("ANDROID","ANDROID")
)

STATUS = ((0, "Draft"), (1, "Publish"))


class Category(models.Model):
    category = models.CharField(max_length=100, choices=CATEGORYCHOICES, unique = True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)
