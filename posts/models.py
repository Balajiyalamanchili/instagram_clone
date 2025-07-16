from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from cloudinary.models import CloudinaryField
import uuid


class Posts(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_img = CloudinaryField('image', blank=True, null=True,default='https://res.cloudinary.com/dtpo9ceis/image/upload/v1752649954/afwhofteawmgxenoxswj.jpg')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user.username}'s Post"
    

class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE ,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}'