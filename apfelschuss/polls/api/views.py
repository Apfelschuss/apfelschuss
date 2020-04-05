from rest_framework import viewsets

from apfelschuss.polls.api.permissions import IsAuthorOrReadOnly
from apfelschuss.polls.api.serializers import CategorySerializer, PollSerializer
from apfelschuss.polls.models import Category, Poll


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    lookup_field = "slug"
    serializer_class = PollSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    lookup_field = "slug"
    serializer_class = CategorySerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    