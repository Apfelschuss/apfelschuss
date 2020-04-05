from rest_framework import serializers

from apfelschuss.polls.models import Category, Poll


class PollSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    thumbnail = serializers.FileField(use_url=True)
    admin_brochure = serializers.FileField(use_url=True)

    class Meta:
        model = Poll
        exclude = ["updated_at", "author"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d. %B %Y")

class CategorySerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        exclude = ["updated_at", "author"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d. %B %Y")
