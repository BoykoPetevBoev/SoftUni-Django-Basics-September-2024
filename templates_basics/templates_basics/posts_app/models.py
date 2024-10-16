from django.db import models

class LanguageChoices(models.TextChoices):
    PYTHON = "py", "Python"
    JAVASCRIPT = "js", "JavaScript"
    C = "c", "C"
    OTHER = "other", "Other"

class Post(models.Model):
    title = models.CharField(
        max_length=100
    )
    
    content = models.TextField()
    
    author = models.CharField(
        max_length=30
    )
    
    created_at = models.DateField(
        auto_now_add=True
    )
    
    languages = models.CharField(
        max_length=30,
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER
    )
