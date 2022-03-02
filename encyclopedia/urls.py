from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/add", views.add, name="add"),
    path("wiki/edit/<str:title>", views.edit, name="edit"),
    path("wiki/new", views.new, name="new"),
    path("wiki/random", views.randomPage, name="random"),
    path("wiki/save", views.save, name="save"),
    path("wiki/search", views.search, name="search"),
    path("wiki/<str:title>", views.entry, name="entry")
]