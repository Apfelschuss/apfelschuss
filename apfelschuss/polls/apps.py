from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = "apfelschuss.polls"
    verbose_name = "polls"

    def ready(self):
        import apfelschuss.polls.signals
