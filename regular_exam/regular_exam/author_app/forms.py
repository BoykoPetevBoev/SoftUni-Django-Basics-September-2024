from django import forms

from regular_exam.author_app.models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }
        
class CreateAuthorForm(AuthorForm):
    class Meta(AuthorForm.Meta):
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']

class EditAuthorForm(AuthorForm):
    class Meta(AuthorForm.Meta):
        fields = ['first_name', 'last_name', 'pets_number', 'info', 'image_url']
        labels = {
            'image_url': 'Profile Image URL',
        }

class DeleteAuthorForm(AuthorForm):
    pass