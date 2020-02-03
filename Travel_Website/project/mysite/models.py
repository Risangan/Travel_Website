from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(User):

    def __str__(self):
        return self.username

class Review(models.Model):
    country = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    country_review = models.CharField(max_length=1000)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.country

    def __str__(self):
        return self.title

    def __str__(self):
        return self.country_review


