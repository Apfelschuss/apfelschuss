from django.urls import reverse, resolve


class TestUrls:

    def test_detail_url(self):
        path = reverse('polls:polls_single', kwargs={'slug': 1})
        assert resolve(path).view_name == 'polls:polls_single'
