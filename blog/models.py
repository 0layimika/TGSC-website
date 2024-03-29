from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"
    def summary(self):
        return self.content[:150]
class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    opinion = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opinion
