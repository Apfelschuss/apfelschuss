from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings

from model_utils.fields import StatusField
from model_utils import Choices

from apfelschuss.utils.unique_slug_generator import unique_slug_generator

# Register your models here.
class Poll(models.Model):
    STATUS = Choices('draft', 'published')
    status = StatusField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=240, verbose_name="Poll title")
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="polls")

    def __str__ (self):
        return self.title
