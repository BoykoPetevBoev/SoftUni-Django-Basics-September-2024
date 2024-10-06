from django.contrib import admin

from workshop_petstagram.photos_app.models import Photo

# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_tagget_pets')
    
    @staticmethod
    def get_tagget_pets(obj):
        return ', '.join([str(pet) for pet in obj.tagged_pets.all()])
