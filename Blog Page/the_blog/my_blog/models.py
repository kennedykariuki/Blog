from django.db import models
from datetime import datetime , date
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length= 255)
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.SET_NULL , null = True )
    publication_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title + " | " + str(self.author)