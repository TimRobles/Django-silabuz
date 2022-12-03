from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.TextField()
    authors = models.TextField()
    average_rating = models.FloatField()
    isbn = models.CharField(max_length=12)
    isbn13 = models.BigIntegerField()
    language_code = models.CharField(max_length=10)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date = models.CharField(max_length=20)
    publisher = models.CharField(max_length=300)
