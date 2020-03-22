from rest_framework import viewsets

from apfelschuss.polls.api.permissions import IsAuthorOrReadOnly
from apfelschuss.polls.api.serializers import PollSerializer
from apfelschuss.polls.models import Poll


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    lookup_field = "slug"
    serializer_class = PollSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    