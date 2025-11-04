from django.contrib import admin
from .models import Post, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Content', 'Created_at', 'Author')
    search_fields = ('Title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'Content', 'Created_at', 'Post', 'Author')
    search_fields = ('Post', )
