from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(3)]) 

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(3)]) 

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    published = models.DateField()

    def __str__(self):
        return self.title