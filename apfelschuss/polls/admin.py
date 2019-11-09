from django.contrib import admin

from translated_fields import TranslatedFieldAdmin

from .models import Author, Category, Poll


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at', 'id']
    readonly_fields = ('created_at', 'updated_at', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'status', 'id']
    readonly_fields = ('created_at', 'updated_at', )


@admin.register(Poll)
class PollAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'featured', 'status', 'id']
    readonly_fields = ('created_at', 'updated_at', )
