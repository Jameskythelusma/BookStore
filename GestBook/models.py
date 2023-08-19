from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=500)
    publication_year = models.DateField(default=timezone.now)

class Review(models.Model):
    Book =models.ForeignKey(Book,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    rating = models.FloatField(max_length=2)
    comment = models.TextField(max_length=1000)

