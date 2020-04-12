from django.contrib import admin

from translated_fields import TranslatedFieldAdmin

from .models import Category, Poll


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'status', 'id']
    readonly_fields = ('created_at', 'updated_at', )


@admin.register(Poll)
class PollAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'category', 'featured', 'status', 'id']
    readonly_fields = ('created_at', 'updated_at', )
