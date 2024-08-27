from django.db import models
from django.core.validators import *
import uuid
from accounts.models import User
from django.core.validators import FileExtensionValidator
from custom.validators import validate_file_size



# Create your models here.

class Topics(models.Model):
    '''
    Represents trends and tags(hashtags)
    '''

    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"This is the {self.name} trend or tag"

class HashTags(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nam

class Tabs(models.Model):
    '''
    Class for each Tab
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    tag = models.ManyToManyField(HashTags, blank=True,related_name='tabs')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.TextField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class TabImage(models.Model):
    tab = models.ForeignKey(Tabs, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Tabs/post_pictures", blank=True, null=True)

class TabVideo(models.Model):
    tab = models.ForeignKey(Tabs, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos_uploaded', blank=True, null=True,
          validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv']), 
          validate_file_size])

class Comment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    Tab = models.ForeignKey(Tabs,on_delete=models.CASCADE)
    # reactions=
    #time
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True) 
    tag = models.ManyToManyField(Topics)


class Polls(models.Model):
    '''
    for Tabs
    '''
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=200, blank=False, null=False )
    Tab = models.ForeignKey(Tabs,on_delete=models.CASCADE)
    percent = models.DecimalField(max_digits=5, default=0, decimal_places=2, validators=[
                                                MinValueValidator(0), 
                                                MaxValueValidator(100)
                                              ])


    

    
