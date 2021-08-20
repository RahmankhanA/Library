from django.db import models

from django.contrib.auth.models import User
from django.conf import settings
from . import util
from moviepy import editor
import os
import shutil
import random


# Create your models here.


class AddVideo(models.Model):
    video=models.FileField(upload_to='static/video')
    libraryName = models.CharField(max_length=31)
    
    coverPicture= models.ImageField(upload_to='static/coverPicture', null=True)
    title= models.CharField(max_length=255)
    description= models.TextField(max_length=10000)
    location= models.CharField(max_length=255)
    videoLanguage = models.CharField(max_length=11, choices=util.languages)
    addClass= models.CharField(max_length=10, choices=util.className )
    subjectCategory= models.CharField(max_length=31, choices=util.subjectCategoryList)

    

  
    def __str__(self):
        return str(self.title)+ " "+ "by " +str(self.libraryName)
