from django.urls import path

from . import views

app_name = "votes"
urlpatterns = [
    path("", views.featured, name="votes_featured"),
    path("latest/", views.category_latest, name="category_latest"),
    path("archive/", views.archive, name="votes_archive"),
    path("search/", views.search, name="votes_search"),
    path("<slug:slug>/", views.voting, name="votes_single"),
]
