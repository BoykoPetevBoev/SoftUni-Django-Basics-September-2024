from django import forms
from workshop_petstagram.photos_app.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"
        
class PhotoAddForm(PhotoForm):
    pass


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']


class PhotoDeleteForm(PhotoForm):
    pass
