from django import template
from ..models import Blog
from django.db.models import Count

register = template.Library()

# Counts the number of existing blog posts
# Another option - @register.simple_tag(name='my_tag')
@register.simple_tag
def total_posts():
    return Blog.objects.count()

# displays blog posts with most comments
@register.simple_tag
def get_most_commented_posts(count = 3):
    return Blog.objects.annotate(
        total_comments = Count('comments')
    ).order_by('-total_comments')[:count]
 