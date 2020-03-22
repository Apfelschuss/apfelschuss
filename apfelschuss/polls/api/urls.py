from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apfelschuss.polls.api import views as qv

router = DefaultRouter()
router.register(r"polls", qv.PollViewSet)

urlpatterns = [
    path("", include(router.urls))
]