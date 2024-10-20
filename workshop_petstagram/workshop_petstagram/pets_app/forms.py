from django import forms

from workshop_petstagram.pets_app.models import Pet


class PetForm(forms.ModelForm):
    class Meta():
        model = Pet
        fields = ["name", "date_of_birth", "personal_photo"]
        
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Add Image Url'})
        }

        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Link to Image',
        }

class PetAddForm(PetForm):
    pass


class PetEditForm(PetForm):
    pass


class PetDeleteForm(PetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True