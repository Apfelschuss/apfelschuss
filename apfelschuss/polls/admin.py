from django.contrib import admin

from translated_fields import TranslatedFieldAdmin

from apfelschuss.polls.models import Poll


@admin.register(Poll)
class PollAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'status', 'id']
    readonly_fields = ('created_at', 'updated_at', )
