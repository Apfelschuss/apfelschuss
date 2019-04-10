from django.urls import path
from . import views

app_name = "votes"
urlpatterns = [
    path('', views.featured, name='featured'),
    path('archive/', views.archive, name='archive'),
    path('<id>/', views.voting, name='single')
]
