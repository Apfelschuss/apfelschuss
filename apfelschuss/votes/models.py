from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.urls import reverse

from filebrowser.fields import FileBrowseField
from tinymce import HTMLField
from translated_fields import TranslatedField

from apfelschuss.votes.utils import unique_slug_generator

User = get_user_model()

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

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
    status = models.IntegerField(
        choices=STATUS,
        default=0
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
        }
    )
    slug = TranslatedField(
        models.SlugField(
            max_length=80,
            verbose_name="Voting URL slug",
        ),
        {
            "de": {"blank": True, "unique": True},
            "fr": {"blank": True, "unique": True},
            "it": {"blank": True, "unique": True},
            "rm": {"blank": True, "unique": True},
            "en": {"blank": True, "unique": True},
        }
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    status = models.IntegerField(
        choices=STATUS,
        default=0
    )
    description = TranslatedField(
        HTMLField(
            verbose_name="Voting description",
        ),
        {
            "de": {"blank": True},
            "fr": {"blank": True},
            "it": {"blank": True},
            "rm": {"blank": True},
            "en": {"blank": True},
        }
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
    video_url = TranslatedField(
        models.URLField(
            max_length=200,
            verbose_name="Youtube embedded URL",
        ),
        {
            "de": {"blank": True},
            "fr": {"blank": True},
            "it": {"blank": True},
            "rm": {"blank": True},
            "en": {"blank": True},
        }
    )
    admin_brochure = TranslatedField(
        FileBrowseField(
            max_length=200,
            directory="uploads/",
            verbose_name="Formal brochure",
        ),
        {
            "de": {"blank": True},
            "fr": {"blank": True},
            "it": {"blank": True},
            "rm": {"blank": True},
            "en": {"blank": True},
        }
    )
    official_pro = models.DecimalField(
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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('votes:votes_single', kwargs={
            'slug': self.slug
        })

    def get_voting_contra(self):
        return 100 - self.official_pro


def slug_save_multilang(sender, instance, *args, **kwargs):
    if not instance.slug_de:
        instance.slug_de = unique_slug_generator(instance, instance.title_de, instance.slug_de, 'de')
    if not instance.slug_fr:
        instance.slug_fr = unique_slug_generator(instance, instance.title_fr, instance.slug_fr, 'fr')
    if not instance.slug_it:
        instance.slug_it = unique_slug_generator(instance, instance.title_it, instance.slug_it, 'it')
    if not instance.slug_rm:
        instance.slug_rm = unique_slug_generator(instance, instance.title_rm, instance.slug_rm, 'rm')
    if not instance.slug_en:
        instance.slug_en = unique_slug_generator(instance, instance.title_en, instance.slug_en, 'en')


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.title, instance.slug)


pre_save.connect(slug_save, sender=Category)
pre_save.connect(slug_save_multilang, sender=Voting)
