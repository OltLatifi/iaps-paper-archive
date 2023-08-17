from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

class Paper(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=255)
    title = models.CharField(max_length=511)
    abstract = models.TextField()
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    publication_date = models.DateTimeField()