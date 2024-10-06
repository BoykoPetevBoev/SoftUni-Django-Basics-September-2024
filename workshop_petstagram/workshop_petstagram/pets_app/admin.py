from django.contrib import admin

from workshop_petstagram.pets_app.models import Pet

# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')