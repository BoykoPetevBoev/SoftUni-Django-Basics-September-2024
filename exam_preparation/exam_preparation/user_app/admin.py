from django.contrib import admin
from exam_preparation.user_app.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
