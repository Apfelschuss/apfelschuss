from django.contrib import admin

from translated_fields import TranslatedFieldAdmin

from .models import Author, Category, Voting

admin.site.register(Author)
admin.site.register(Category)


@admin.register(Voting)
class VotingAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    pass
