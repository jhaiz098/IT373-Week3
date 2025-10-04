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