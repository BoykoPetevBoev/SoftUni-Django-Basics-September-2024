from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


# class Profile(models.Model):
#     pass
class Profile(AbstractUser):
    # username = models.CharField(
    #     unique=True,
    #     max_length=15,
    #     #  TODO add char validation
    # )
    email = models.EmailField(
        unique=True
    )
    age = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )