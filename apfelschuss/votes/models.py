from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from filebrowser.fields import FileBrowseField
from tinymce import HTMLField
from translated_fields import TranslatedField

from apfelschuss.votes.utils import unique_slug_generator

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        )
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        auto_now=True
        )

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(
        max_length=80,
        verbose_name="Voting category title"
        )
    slug = models.SlugField(
        max_length=80,
        unique=True,
        verbose_name="Voting category URL slug",
        blank=True
        )
    voting_date = models.DateTimeField(
        verbose_name="Voting final date"
        )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        )
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        auto_now=True
        )
    published = models.BooleanField(
        default=False
        )
    featured = models.BooleanField(
        default=False,
        verbose_name="Featured category"
        )

    def __str__(self):
        return self.title


class Voting(models.Model):
    title = TranslatedField(
        models.CharField(
            verbose_name="Voting title",
            max_length=160,
        ),
        {
            "de": {"blank": True},
            "fr": {"blank": True},
            "it": {"blank": True},
            "rm": {"blank": True},
            "en": {"blank": True},
        },
    )
    slug =  TranslatedField(
        models.SlugField(
            max_length=80,
            verbose_name="Voting URL slug",
            blank=True
        ),
        {
            "de": {"blank": True, "unique": True},
            "fr": {"blank": True, "unique": True},
            "it": {"blank": True, "unique": True},
            "rm": {"blank": True, "unique": True},
            "en": {"blank": True, "unique": True},
        },
    )
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        auto_now=True
        )
    published = models.BooleanField(
        default=False,
        verbose_name="Voting published"
        )
    description = TranslatedField(
        HTMLField(
            verbose_name="Voting description",
            blank=True,
            ),
            {
                "de": {"blank": True},
                "fr": {"blank": True},
                "it": {"blank": True},
                "rm": {"blank": True},
                "en": {"blank": True},
            },
        )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        )
    thumbnail = FileBrowseField(
        "Thumbnail",
        max_length=200,
        directory="uploads/",
        blank=True,
        )
    video_url = models.URLField(
        max_length=200,
        verbose_name="Youtube embedded URL",
        blank=True
        )
    admin_brochure = FileBrowseField(
        "Formal brochure",
        max_length=200,
        directory="uploads/",
        blank=True,
        )
    admin_pro = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        verbose_name="Final result pro [%]",
        blank=True, null=True
        )
    categories = models.ManyToManyField(
        Category,
        verbose_name="Voting category",
        )
    featured = models.BooleanField(
        default=False,
        verbose_name="Featured voting"
        )
    previous_voting = models.ForeignKey(
        'self',
        related_name='previous',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    next_voting = models.ForeignKey(
        'self',
        related_name='next',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('votes:votes_single', kwargs={
            'slug': self.slug
        })


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.title, instance.slug)


pre_save.connect(slug_save, sender=Category)
pre_save.connect(slug_save, sender=Voting)
