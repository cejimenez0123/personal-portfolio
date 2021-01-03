from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    path('tag/<slug:tag_slug>/', views.all_blogs, name='blog_list_by_tag'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
    path('<int:blog_id>/share/', views.blog_share, name='post_share'),
]