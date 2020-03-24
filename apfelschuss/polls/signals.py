from django.db.models.signals import pre_save
from django.dispatch import receiver

from apfelschuss.polls.models import Category, Poll
from apfelschuss.utils.unique_slug_generator import unique_slug_generator


@receiver(pre_save, sender=Category)
@receiver(pre_save, sender=Poll)
def slug_save(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.title, instance.slug)
