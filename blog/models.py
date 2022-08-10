from django.db import models
from personal_website.settings import AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name}'
class Post(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField()
    content = models.TextField(max_length=2000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    def __str__(self):
        return f'{self.title}'
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




