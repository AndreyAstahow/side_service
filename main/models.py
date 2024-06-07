from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    id = models.BigAutoField
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=300)
    token = models.CharField(max_length=300)

    def get_absolute_url(selt):
        return reverse('post_list')