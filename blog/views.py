from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

def all_blogs(request):
    # All Written blogs
    blogs = Blog.objects.order_by('-date')
    paginator = Paginator(blogs, 10) # Number of blogs per page
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    
    return render(request, 'blog/all_blogs.html', {
        'page': page,
        'count': paginator.count
    })

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
