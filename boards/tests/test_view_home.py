from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from boards.views import home
from boards.models import Board


class BoardHomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('board_home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        url = reverse('board_home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/board/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))

