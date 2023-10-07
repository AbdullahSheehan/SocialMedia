from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userInfo')
    fullname = models.CharField(max_length=100, blank=True)
    profilepic = models.ImageField(upload_to="profilepics/", blank=True)
    dob = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    bio = models.TextField(max_length=150, blank=True)

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    time = models.DateTimeField(auto_now_add=True)