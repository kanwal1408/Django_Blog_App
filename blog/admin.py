from django.contrib import admin
from .models import PostModel, Comment

# Register your models here.


class PostModelAdmin(admin.ModelAdmin): # to show date_created column along title in admin page
    list_display = ('title','date_created')

admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Comment)