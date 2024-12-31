from django.db import models
from django import forms
from musician.models import Musician
from datetime import date

# Create your models here.

class Album(models.Model):
    name=models.CharField(max_length=50)
    musician=models.ForeignKey(Musician,on_delete=models.CASCADE)
    release=models.DateField(default=date.today)
    levels=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    rating=models.CharField(max_length=10,choices=levels)
    
    def __str__(self) -> str:
        return f"Album Name: {self.name}"
    
