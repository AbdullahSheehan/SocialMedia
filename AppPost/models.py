from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted')
    image = models.ImageField(upload_to='Post_Pictures/')
    captions = models.CharField(max_length=264, blank=True)
    upload = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-upload', ]

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likedpost')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} liked {}".format(self.user, self.post)
