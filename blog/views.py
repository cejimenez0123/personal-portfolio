from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator
from .forms import EmailPostForm
from django.core.mail import send_mail

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

# Share blog using email/user form
def blog_share(request, blog_id):
    # Retrieve Blog by ID
    blog = get_object_or_404(Blog, id = blog_id)
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            blog_url = request.build_absolute_uri(f'/blog/{blog_id}')
            all_blogs = request.build_absolute_uri(f'/blog')
            subject = f"{cd['name']} recommends you read " \
            f"{blog.title}"
            message = f"Hey. Check out the blog post '{blog.title}' at {blog_url} in Ronard Luna's blog. See all blog posts here {all_blogs} \n\n" \
                      f"{cd['name']}\'s comments: \n\n{cd['comments']}"
            send_mail(subject, message, 'ronarddevelops@gmail.com',
                       [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/share.html', {'blog': blog,
                                                'form': form,
                                                'sent': sent })