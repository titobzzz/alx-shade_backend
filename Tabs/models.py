from django.db import models
from django.core.validators import *
import uuid
from accounts.models import User
from django.core.validators import FileExtensionValidator
from custom.validators import validate_file_size
from django.contrib.staticfiles.storage import staticfiles_storage



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

def upload_to_static(instance, filename):
    return f'images/{filename}'

class TabMedia(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )
    
    tab = models.ForeignKey(Tabs, related_name='media', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, db_index=True)
    file = models.FileField(
        storage=staticfiles_storage,
        upload_to=upload_to_static,
        blank=True, 
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'mov', 'avi', 'mp4', 'webm', 'mkv']),
            validate_file_size
        ]
    )
    duration = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.media_type} for {self.tab}"
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


    

    
