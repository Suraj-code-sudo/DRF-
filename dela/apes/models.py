import email
from django.db import models
from numpy import true_divide



# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title