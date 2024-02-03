# urls.py
from django.urls import path

from .views import blog_list, search_view

urlpatterns = [
    path("", blog_list, name="blog_list"),
    path("search/", search_view, name="search_view"),
]
