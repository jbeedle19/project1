from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/add", views.add, name="add"),
    path("wiki/new", views.new, name="new"),
    path("wiki/search", views.search, name="search"),
    path("wiki/<str:title>", views.entry, name="entry")
]