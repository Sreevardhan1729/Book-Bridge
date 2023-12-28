from django.db import models

# Create your models here.
class Book(models.Model):
    username = models.CharField(max_length=255)
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    year_of_publication = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=100)
    has_image = models.CharField(max_length=255)
    book_description = models.TextField()
    state_location = models.CharField(max_length=255)