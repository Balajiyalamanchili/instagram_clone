from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from cloudinary.models import CloudinaryField



class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_img = CloudinaryField('image', blank=True, null=True)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username}'s Post"