from django.db import models
# from django.db.models.deletion import CASCADE
from django.conf import settings 
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def str(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts-detail', kwargs={'pk':self.pk})