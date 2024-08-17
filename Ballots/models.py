from django.db import models
from django.core.validators import *
import uuid
from accounts.models import User



# Create your models here.

class Topics(models.Model):
    '''
    Represents trends and tags
    '''

    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"This is the {self.name} trend or tag"



class Ballots(models.Model):
    '''
    class for each ballot Posts 
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    tag = models.ManyToManyField(Topics)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    images= models.ImageField(upload_to="Ballots/ballot_pictures",blank=True, null=True)
    text_content = models.TextField(max_length=500, null=True, blank=True)
    # reactions= models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True) 


class Comment(models.Model):
    ''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    ballot = models.ForeignKey(Ballots,on_delete=models.CASCADE)
    # reactions=
    #time
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True) 
    tag = models.ManyToManyField(Topics)


class Poll(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=200, blank=False, null=False )
    ballot = models.ForeignKey(Ballots,on_delete=models.CASCADE)
    percent = models.DecimalField(max_digits=5, default=0, decimal_places=2, validators=[
                                                MinValueValidator(0), 
                                                MaxValueValidator(100)
                                              ])


    

    
