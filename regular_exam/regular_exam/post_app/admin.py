from django.contrib import admin

from regular_exam.post_app.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass