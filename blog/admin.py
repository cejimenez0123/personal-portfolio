from django.contrib import admin
from .models import Blog

# Make the blog display in the admin site
admin.site.register(Blog)

