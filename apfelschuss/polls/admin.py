from django.contrib import admin

from translated_fields import TranslatedFieldAdmin

from .models import Author, Category, Poll

admin.site.register(Author)
admin.site.register(Category)


@admin.register(Poll)
class PollAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    pass
