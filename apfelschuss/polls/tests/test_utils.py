from django.contrib.auth import get_user_model
from django.test import TestCase

from apfelschuss.polls.models import Category, Poll

User = get_user_model()


class CategoryTestCase(TestCase):
    def setUp(self):
        owner = User.objects.create_user(
            username='test',
            email='test@test.ch',
            password='top_secret'
            )
        Category.objects.create(
            title="This is a category title",
            poll_date="2019-04-19T21:19:16.917697+00:00",
            owner=owner
            )
        Category.objects.create(
            title="This is a category title",
            poll_date="2019-04-19T21:19:16.917697+00:00",
            owner=owner
            )

    def test_check_slugs(self):
        object_1 = Category.objects.get(pk=1)
        object_2 = Category.objects.get(pk=2)

        self.assertEqual(object_1.slug, 'this-is-a-category-title')
        self.assertEqual(object_2.slug, 'this-is-a-category-title-2')


class PollTestCase(TestCase):
    def setUp(self):
        owner = User.objects.create_user(
            username='test',
            email='test@test.ch',
            password='top_secret'
            )
        category = Category.objects.create(
            title="This is a category title",
            poll_date="2019-04-19T21:19:16.917697+00:00",
            owner=owner
            )
        Poll.objects.create(
            title_en="This is a poll title",
            owner=owner,
            category=category
            )
        Poll.objects.create(
            title_en="This is a poll title",
            owner=owner,
            category=category
            )

    def test_check_slugs(self):
        object_1 = Poll.objects.get(pk=1)
        object_2 = Poll.objects.get(pk=2)

        self.assertEqual(object_1.slug_en, 'this-is-a-poll-title')
        self.assertEqual(object_2.slug_en, 'this-is-a-poll-title-2')
