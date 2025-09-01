from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    tmbdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField() # Can rate between 1-10

    class Meta:
        unique_together = ('user', 'movie')