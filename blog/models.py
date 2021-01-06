from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to = 'blog/images/', blank = True)
    url = models.URLField(blank = True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail')

class Comment(models.Model):
    post = models.ForeignKey(Blog, 
                            on_delete = models.CASCADE,
                            related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default= True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    
   