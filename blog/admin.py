from django.contrib import admin
from .models import Comments
from .models import Post, Visit
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_dysplay = ('title', 'author')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_dysplay = ('name', 'text_comment')


@admin.register(Visit)
class PostAdmin(admin.ModelAdmin):
    list_dysplay = ('ip_addr', 'count', 'data')
