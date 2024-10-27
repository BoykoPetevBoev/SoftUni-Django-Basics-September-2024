from django.contrib import admin

from regular_exam.author_app.models import Author

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass