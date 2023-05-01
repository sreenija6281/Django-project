from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Work(models.Model):
    LINK_CHOICES = (
        ('Youtube', 'Youtube'),
        ('Instagram', 'Instagram'),
        ('Other', 'Other'),
    )
    link = models.URLField()
    work_type = models.CharField(max_length=20, choices=LINK_CHOICES)
    artists = models.ManyToManyField('Artist')

class Artist(models.Model):
    name = models.CharField(max_length=100)
