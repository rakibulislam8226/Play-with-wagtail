from django.shortcuts import render

from .models import BlogPage


def blog_list(request):
    blog_posts = BlogPage.objects.live().public()
    return render(request, "blog/blog_list.html", {"blog_posts": blog_posts})
