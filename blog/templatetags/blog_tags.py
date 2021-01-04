from django import template
from ..models import Blog

register = template.Library()

@register.simple_tag
def total_posts():
    return Blog.objects.count()