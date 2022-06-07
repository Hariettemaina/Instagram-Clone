import uuid
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt

from django.db.models.signals import post_save


class posts(models.Model):
    # title field
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images',null=True)
    post_date = models.DateTimeField(auto_now_add=True,null=True)
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')
    liked= models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    # profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like_count = models.IntegerField(default=0)

    

    @classmethod
    # search images using image name
    def search_image_name(cls, search_term):
        images = cls.objects.filter(
        title__icontains=search_term)
        return images   

    @property
    def saved_comments(self):
        return self.comments.all() 

    def _str_(self):
        return self.user.username       

    def _str_(self):
        return self.title        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

  

LIKE_CHOICES={
    ('Like','Like'),
    ('Dislike','Dislike',)
}
class Likes(models.Model):
    image = models.ForeignKey(posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='like',max_length=10)

    def _str_(self):
        return self.value
    
    def __str__(self):
        return self.user
    

    # def __str__(self):
    #     return self.user


class Comment(models.Model):
    comment = models.CharField(max_length=250)
    image = models.ForeignKey(posts,on_delete = models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')

    @classmethod
    def display_comment(cls,image_id):
        comments = cls.objects.filter(image_id = image_id)
        return comments