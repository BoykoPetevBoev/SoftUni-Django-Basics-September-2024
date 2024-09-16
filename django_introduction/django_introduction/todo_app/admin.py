from django.contrib import admin

from django_introduction.todo_app.models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass