from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(blank=True,max_length=10)
    profile_pic = CloudinaryField('image', blank=True, null=True,default='https://res.cloudinary.com/dtpo9ceis/image/upload/v1752648759/vswcnd9rltn1mqwr2rwl.jpg')
    followers = models.ManyToManyField(User,related_name='followers',blank=True)
    following = models.ManyToManyField(User,related_name='following',blank=True)

    def __str__(self):
        return self.user.username
