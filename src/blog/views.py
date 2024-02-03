from django.shortcuts import render

from wagtail.models import Page
from wagtail.search.backends import get_search_backend

from .models import BlogPage


def blog_list(request):
    blog_posts = BlogPage.objects.live().public()
    return render(request, "blog/blog_list.html", {"blog_posts": blog_posts})


def search_view(request):
    query = request.GET.get("q", "")

    # Use Wagtail's search backend to get search results
    search_backend = get_search_backend()
    search_results = search_backend.search(query, Page)

    context = {
        "query": query,
        "search_results": search_results,
    }

    return render(request, "search/search_results.html", context)
