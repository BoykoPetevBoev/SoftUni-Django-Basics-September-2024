from django import forms

from templates_basics.posts_app.models import LanguageChoices, Post

    #     widget=forms.Select(choices=POSITION)


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=40,
        label='',
        required=False
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        
        # widgets = {
        #     'title': forms.CharField()
        # }
        
        # labels = {
        #     'title': 'Title label'
        # }
        
        # error_messages = {
        #     'title': {
        #         'required': "This filed is required!"
        #     }
        # }
        
        # help_text = {
        #     'title': 'This is the title'
        # }


class PostCreateForm(PostForm):
    pass


class PostEditForm(PostForm):
    pass


class PostDeleteForm(PostForm):
    disabled_fields = ('__all__',)
    
    

class PersonForm (forms.Form):
    POSITION = (
        (1, "Junior"),
        (2, "Mid"),
        (3, "Senior"),
    )
    
    name = forms.CharField(
        max_length=10,
        label='Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your first and last name'})
    )
    
    age = forms.IntegerField(
        
    )
    
    # position1 = forms.IntegerField(
    #     widget=forms.Select(choices=POSITION)
    # )
    
    position2 = forms.ChoiceField(
        choices=POSITION
    )

    position3 = forms.ChoiceField(
        widget=forms.RadioSelect(),  
        choices=POSITION
    )
    
    description = forms.CharField(
        widget=forms.Textarea(),
        max_length=100
    )
    
    policy = forms.BooleanField()
