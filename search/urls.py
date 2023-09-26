from django.urls import include, re_path
from search.views import search

urlpatterns = [
    re_path(r'^$', search, name="search"),
]
