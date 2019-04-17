from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from tinymce import HTMLField

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=80)
    voting_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Voting(models.Model):
    title = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    description = HTMLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    video_url = models.URLField(max_length=200)
    pro_url = models.URLField(max_length=200)
    contra_url = models.URLField(max_length=200)
    admin_url = models.URLField(max_length=200)
    admin_brochure = models.FileField(upload_to='uploads/')
    admin_pro = models.DecimalField(max_digits=4, decimal_places=1)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)
    previous_voting = models.ForeignKey(
        'self',
        related_name='previous',
        on_delete=models.SET_NULL,
        blank=True, null=True)
    next_voting = models.ForeignKey(
        'self',
        related_name='next',
        on_delete=models.SET_NULL,
        blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('votes:votes_single', kwargs={
            'id': self.id
        })
