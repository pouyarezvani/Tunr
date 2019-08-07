from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Artist(models.Model):
  name = models.CharField(max_length=100)
  nationality = models.CharField(max_length=100)
  photo_url = models.TextField()
  spotify_link = models.TextField(default='https://www.spotify.com/')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artists')
  def __str__(self):
    return self.name
  
  def hello(self):
    return f"I am {self.name}"

class Song(models.Model):
  spotify_preview = models.TextField(default="https://www.spotify.com/")
  title = models.CharField(max_length=100, default="untitled")
  genre = models.CharField(max_length=100, default="unassigned")
  length = models.PositiveIntegerField(default="2")
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')

  def __str__(self):
    return f"{self.title}-{self.artist}"