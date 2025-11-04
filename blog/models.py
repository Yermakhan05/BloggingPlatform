from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=250)
    Content = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title


class Comment(models.Model):
    Content = models.TextField()
    Created_at = models.DateTimeField()
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
