from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Bio = models.TextField()
    ProfilePicture = models.ImageField(upload_to='profile_pictures/')


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
