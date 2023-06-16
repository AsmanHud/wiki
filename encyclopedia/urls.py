from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entrytitle>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("edit/<str:entrytitle>", views.edit, name="edit"),
    path('randompage', views.randompage, name='randompage'),
]