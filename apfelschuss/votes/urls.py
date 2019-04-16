from django.urls import path
from . import views

app_name = "votes"
urlpatterns = [
    path('', views.featured, name='votes_featured'),
    path('archive/', views.archive, name='votes_archive'),
    path('search/', views.search, name='votes_search'),
    path('<int:id>/', views.voting, name='votes_single')
]
