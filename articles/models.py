from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category
    
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    image = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment
    
    
    
    
    
    