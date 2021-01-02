from django.contrib import admin
from .models import Blog, Comment

# Make the blog display in the admin site
admin.site.register(Blog)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'

# Make comments display
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')