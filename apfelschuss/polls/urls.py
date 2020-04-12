from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.featured, name="polls_featured"),
    path("latest/", views.category_latest, name="category_latest"),
    path("archive/", views.archive, name="polls_archive"),
    path("search/", views.search, name="polls_search"),
    path("<slug:slug>/", views.poll, name="polls_single"),
]
