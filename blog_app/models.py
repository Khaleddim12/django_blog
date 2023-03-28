from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField 
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse('blog_app:CategoryListView')
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null= True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'posts')
    likes = models.ManyToManyField(User, related_name='blog_posts',blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    
    def number_of_likes(self):
        return self.likes.count()
    
    
    def __str__(self):
        return self.title + ' by ' + self.author.username
    
    def get_absolute_url(self):
        return reverse('blog_app:PostDetailView', kwargs={'pk': self.pk})