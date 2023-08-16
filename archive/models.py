from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

class Paper(models.Model):
    title = models.CharField(max_length=511)
    abstract = models.TextField()
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)