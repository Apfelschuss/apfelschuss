from django.urls import path
from . import views

app_name = "votes"
urlpatterns = [
<<<<<<< Updated upstream
    path('', views.featured, name='featured'),
    path('archive/', views.archive, name='archive'),
    path('search/', views.search, name='search'),
    path('<id>/', views.voting, name='single')
=======
    path('', views.voting, name='voting-featured'),
    #path('<id>/', voting, name='voting-detail'),
    path('archive/', views.archive, name='voting-archive'),
>>>>>>> Stashed changes
]
