from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment
from django.core.paginator import Paginator
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from taggit.models import Tag

def all_blogs(request, tag_slug=None):
    # All Written blogs
    blogs = Blog.objects.order_by('-date')
    tag = None

    # Search blogs by tag
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        blogs = blogs.filter(tags__in=[tag])

    # Pagination logic
    paginator = Paginator(blogs, 10) # Number of blogs per page
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    
    return render(request, 'blog/all_blogs.html', { 'page': page,
                                                    'count': paginator.count,
                                                    'tag': tag
    })

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)

    # List of active comments for this post
    comments = blog.comments.filter(active = True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit = False)
            # Assign the current post to the comment
            new_comment.post = blog
            # Save the comment to the databasa
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 
                'blog/detail.html', 
                {'blog': blog, 
                'comments': comments, 
                'new_comment': new_comment, 
                'comment_form': comment_form})

# Share blog using email
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