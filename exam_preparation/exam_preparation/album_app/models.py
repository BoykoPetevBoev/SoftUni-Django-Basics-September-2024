from django.db import models
from django.core.validators import MinValueValidator
# from exam_preparation.user_app.models import Profile
# Create your models here.

GENRE_CHOICES = {
    "POP": "Pop Music", 
    "JAZZ": "Jazz Music",
    "R&B": "R&B Music",
    "ROCK": "Rock Music",
    "COUNTRY": "Country Music",
    "DANCE": "Dance Music",
    "HIPHOP": "Hip Hop Music",
    "OTHER": "Other"
}

class Album(models.Model):
    album_name = models.CharField(
        unique=True,
        max_length=30
    )
    artist = models.CharField(
        max_length=30
    )
    genre = models.CharField(
        max_length=30,
        choices=GENRE_CHOICES
    )
    description = models.TextField(
        blank=True
    )
    image_url = models.URLField()
    price = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )
    # owner = models.OneToOneField(
    #     Profile,
    #     on_delete=models.CASCADE
    # )
    
    
    