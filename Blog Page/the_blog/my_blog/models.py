from django.db import models
from datetime import datetime , date
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User , on_delete= models.CASCADE)
    body = models.TextField()
    publication_date = models.DateField(auto_now_add = True )

    def __str__(self):
        return self.title + " | " + str(self.author)