from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save

from filebrowser.fields import FileBrowseField
from model_utils.fields import StatusField
from model_utils import Choices
from tinymce import HTMLField

from apfelschuss.utils.unique_slug_generator import unique_slug_generator

class Category(models.Model):
    STATUS = Choices('draft', 'published')
    status = StatusField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=240, verbose_name="Poll category title")
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    poll_date = models.DateTimeField(verbose_name="Category final date")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="categories")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Poll(models.Model):
    STATUS = Choices('draft', 'published')
    status = StatusField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=240, verbose_name="Poll title")
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    description = HTMLField(verbose_name="Poll description", blank=True)
    thumbnail = FileBrowseField(
        "Thumbnail",
        max_length=255,
        directory="uploads/",
        blank=True,
        )
    video_url = models.URLField(
        max_length=255,
        verbose_name="Youtube embedded URL",
        blank=True,
        )
    admin_brochure = FileBrowseField(
        max_length=255,
        directory="uploads/",
        verbose_name="Formal brochure",
        blank=True,
        )
    featured = models.BooleanField(
        default=False,
        verbose_name="Featured poll"
        )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Poll category",
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="polls")

    def __str__ (self):
        return self.title
