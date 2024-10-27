from django.db import models
from django.core.validators import MinLengthValidator
from regular_exam.author_app.validators import LettersOnlyValidator, PasscodeValidator


# Create your models here.
class Author (models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            LettersOnlyValidator()
        ],
    )
    
    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            LettersOnlyValidator()
        ],
    )
    
    passcode = models.CharField(
        validators=[
            PasscodeValidator(),
        ],
        help_text="Your passcode must be a combination of 6 digits"
    )
    
    pets_number = models.PositiveIntegerField()
    
    info = models.TextField(
        blank=True, 
        null=True
    )
    
    image_url = models.URLField(
        blank=True, 
        null=True
    )    
    