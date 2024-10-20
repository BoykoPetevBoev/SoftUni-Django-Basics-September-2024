from django.contrib import admin

from workshop_petstagram.common_app.models import Comment, Like

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass