from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    texy = models.TextField()
    author = models.ForeignKey(User)
    created_date = models.DateTimeField()
    publish_date = models.DateTimeField()