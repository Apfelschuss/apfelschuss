from django.contrib.auth import get_user_model
from django.test import TestCase

from apfelschuss.votes.models import Author, Category, Voting

User = get_user_model()


class CategoryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@test.ch',
            password='top_secret'
            )
        author = Author.objects.create(user=self.user)
        Category.objects.create(
            title="This is a category title",
            voting_date="2019-04-19T21:19:16.917697+00:00",
            author=author
            )
        Category.objects.create(
            title="This is a category title",
            voting_date="2019-04-19T21:19:16.917697+00:00",
            author=author
            )

    def test_check_slugs(self):
        object_1 = Category.objects.get(pk=1)
        object_2 = Category.objects.get(pk=2)

        self.assertEqual(object_1.slug, 'this-is-a-category-title')
        self.assertEqual(object_2.slug, 'this-is-a-category-title-2')


class VotingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@test.ch',
            password='top_secret'
            )
        author = Author.objects.create(user=self.user)
        Voting.objects.create(
            title_en="This is a voting title",
            author=author
            )
        Voting.objects.create(
            title_en="This is a voting title",
            author=author
            )

    def test_check_slugs(self):
        object_1 = Voting.objects.get(pk=1)
        object_2 = Voting.objects.get(pk=2)

        self.assertEqual(object_1.slug_en, 'this-is-a-voting-title')
        self.assertEqual(object_2.slug_en, 'this-is-a-voting-title-2')
