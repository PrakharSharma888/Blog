from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User,auth
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) #many to one
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-details', kwargs={'pk':self.pk})